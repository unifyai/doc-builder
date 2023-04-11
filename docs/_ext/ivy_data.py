from sphinx.application import Sphinx
from sphinx.ext.autodoc import DataDocumenter

class IvyDataDocumenter(DataDocumenter):
    """Data attributes can't have a __doc__ attribute, but Epydoc can detect the docs
    from the module code. This documenter is user to replace the module name after the
    DataDocumenter has been run."""
    objtype = 'ivydata'
    directivetype = DataDocumenter.objtype
    priority = DataDocumenter.priority - 10

    def add_directive_header(self, sig: str) -> None:
        super().add_directive_header(sig)

        for i, line in enumerate(self.directive.result):
            if line.startswith("   :module: "):
                self.directive.result[i] = "   :module: ivy"
                break


def setup(app: Sphinx):
    app.setup_extension("sphinx.ext.autodoc")
    app.add_autodocumenter(IvyDataDocumenter)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
    }

from docutils.statemachine import StringList

from sphinx.application import Sphinx
from sphinx.ext.autodoc import MethodDocumenter

def _skip(obj, skippable_method_attributes):
    return any(
        [
            all(
                [
                    getattr(obj, key, None) == value
                    for key, value in match.items()
                ]
            )
            for match in skippable_method_attributes
        ]
    )

def skip_method(app: Sphinx, what, name, obj, skip, options):
    return skip or _skip(obj, app.config.skippable_method_attributes)

class SkippableMethodDocumenter(MethodDocumenter):
    objtype = 'skippablemethod'
    directivetype = MethodDocumenter.objtype
    priority = MethodDocumenter.priority - 10

    def add_directive_header(self, sig: str) -> None:
        if _skip(self.object, self.env.config.skippable_method_attributes):
            return

        super().add_directive_header(sig)

    def add_content(self,
                    more_content: StringList | None
                    ) -> None:
        if _skip(self.object, self.env.config.skippable_method_attributes):
            return

        super().add_content(more_content)


def setup(app: Sphinx):
    app.setup_extension("sphinx.ext.autodoc")
    app.add_autodocumenter(SkippableMethodDocumenter)
    app.connect("autodoc-skip-member", skip_method)
    app.add_config_value("skippable_method_attributes", [], "env")

    return {
        "version": "0.1",
        "parallel_read_safe": True,
    }

from docutils.statemachine import StringList

from sphinx.application import Sphinx
from sphinx.ext.autodoc import MethodDocumenter

class SkippableMethodDocumenter(MethodDocumenter):
    objtype = 'skippablemethod'
    directivetype = MethodDocumenter.objtype
    priority = MethodDocumenter.priority - 10

    def skip(self) -> bool:
        return any(
            [
                all(
                    [
                        getattr(self.object, key, None) == value
                        for key, value in match.items()
                    ]
                )
                for match in self.env.config.skippable_method_attributes
            ]
        )

    def add_directive_header(self, sig: str) -> None:
        if self.skip():
            return

        super().add_directive_header(sig)

    def add_content(self,
                    more_content: StringList | None
                    ) -> None:
        if self.skip():
            return

        super().add_content(more_content)


def setup(app: Sphinx):
    app.setup_extension("sphinx.ext.autodoc")
    app.add_autodocumenter(SkippableMethodDocumenter)
    app.add_config_value("skippable_method_attributes", [], "env")

    return {
        "version": "0.1",
        "parallel_read_safe": True,
    }

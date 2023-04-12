from pathlib import Path

from docutils.parsers.rst import directives
from docutils import nodes
from docutils.statemachine import ViewList

import sphinx
from sphinx.ext.autosummary import Autosummary
from sphinx.application import Sphinx
from sphinx.util import logging
from sphinx.errors import ExtensionError

logger = logging.getLogger(__name__)


class CustomAutosummary(Autosummary):
    new_option_spec = {
        "hide-table": directives.flag,
    }

    option_spec = {
        **Autosummary.option_spec,
        **new_option_spec,
    }

    def run(self):
        if all([option not in self.options for option in self.new_option_spec.keys()]):
            return super().run()

        return_nodes = super().run()
        if "hide-table" in self.options:
            self.check_for_prequisite("hide-table", "toctree")
            # Auto summary produces some tables, and a toc tree at the end.
            # We only need the latter.
            return_nodes = return_nodes[-1:]


        return return_nodes

    def check_for_prequisite(self, option, prequisite, included=True):
        if included and prequisite not in self.options:
            raise ExtensionError(
                f"'{option}' option is only valid when using '{prequisite}' option."
            )
        elif not included and prequisite in self.options:
            raise ExtensionError(
                f"'{option}' option is not valid when using '{prequisite}' option."
            )


def setup(app: Sphinx):
    app.setup_extension("sphinx.ext.autosummary")
    app.add_directive("autosummary", CustomAutosummary, override=True)

    return {
        "version": sphinx.__display_version__,
        "parallel_read_safe": True,
    }

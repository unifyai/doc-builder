# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath(".."))


# -- Project information -----------------------------------------------------

project = "Ivy"
copyright = "2020-2023, Ivy Team"
author = "Ivy Team"

# The full version, including alpha/beta/rc tags
release = "1.0"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "docs._ext.custom_autosummary",
    "docs._ext.discussion_linker",
    "docs._ext.custom_builder",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates", "_html_templates"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_css_files = [
    "css/custom.css",
]

html_theme_options = {
    "navbar_center": ["empty"],
    "header_links_before_dropdown": 100,
    "secondary_sidebar_items": ["sidebar-nav-bs", "page-toc"],
    "logo": {
        "image_light": "https://github.com/unifyai/unifyai.github.io/blob/master/img/externally_linked/logo.png?raw=true",  # noqa: E501
        "image_dark": "https://github.com/unifyai/unifyai.github.io/blob/master/img/externally_linked/logo_dark.png?raw=true",  # noqa: E501
    },
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/unifyai/ivy",
            "icon": "fa-brands fa-square-github",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/letsunifyai",
            "icon": "fa-brands fa-square-twitter",
        },
    ],
}

html_sidebars = {"**": ["custom-toc-tree", "ivy-libraries"]}

html_title = "Ivy Documentation"

html_favicon = (
    "https://github.com/unifyai/unifyai.github.io"
    + "/blob/master/img/externally_linked/ivy_logo_only.png?raw=true"
)

autodoc_member_order = "alphabetical"

ivy_toctree_caption_map = {
    "ivy.functional.ivy": "Functions",
    "ivy.stateful": "Framework classes",
    "ivy.nested_array": "Nested array",
    "ivy.utils": "Utils",
    "ivy_tests.test_ivy.helpers": "Testing",
}

discussion_channel_map = {
    "ivy.data_classes.array.array": ["1000042910831620176", "1028296936203235359"],
    "ivy.data_classes.container.container": [
        "1000042831928381591",
        "1028297229980668015",
    ],
    "ivy.functional.ivy.activations": ["1000043490329251890", "1028298682614947850"],
    "ivy.functional.ivy.compilation": ["1000043526849056808", "1028298745726648371"],
    "ivy.functional.ivy.constants": ["1000043690254946374", "1028298780715536454"],
    "ivy.functional.ivy.creation": ["1000043690254946374", "1028298816526499912"],
    "ivy.functional.ivy.data_type": ["1000043749088436315", "1028298847950225519"],
    "ivy.functional.ivy.device": ["1000043825085026394", "1028298877998211204"],
    "ivy.functional.ivy.elementwise": ["1000043825085026394", "1028298919488278589"],
    "ivy.functional.ivy.extensions": ["1028272402624434196", "1028298957870354542"],
    "ivy.functional.ivy.general": ["1000043859973247006", "1028298984806170634"],
    "ivy.functional.ivy.gradients": ["1000043921633722509", "1028299026501750826"],
    "ivy.functional.ivy.layers": ["1000043967989162005", "1028299061092175872"],
    "ivy.functional.ivy.linear_algebra": ["1000044022942933112", "1028299123046240366"],
    "ivy.functional.ivy.losses": ["1000044049333485648", "1028299153148739646"],
    "ivy.functional.ivy.manipulation": ["1000044082489466951", "1028299188112461986"],
    "ivy.functional.ivy.meta": ["1000044106959044659", "1028299213701914674"],
    "ivy.functional.ivy.nest": ["1000044136000393326", "1028299238964219924"],
    "ivy.functional.ivy.norms": ["1000044163070447626", "1028299276985581598"],
    "ivy.functional.ivy.random": ["1000044191658815569", "1028299348800450590"],
    "ivy.functional.ivy.searching": ["1000044227247484980", "1028299387258019950"],
    "ivy.functional.ivy.sorting": ["1000044274148184084", "1028299468908535841"],
    "ivy.functional.ivy.statistical": ["1000044336479731872", "1028299556955361351"],
    "ivy.functional.ivy.utility": ["1000044369044312164", "1028299594733457428"],
    "ivy.stateful.activations": ["1000043360297439272", "1028300670505336893"],
    "ivy.stateful.converters": ["1000043009758474310", "1028300734355226725"],
    "ivy.stateful.initializers": ["1000043132706115654", "1028300779083272252"],
    "ivy.stateful.layers": ["1000043206840426686", "1028300805209604178"],
    "ivy.stateful.module": ["1000043315267387502", "1028300829905653780"],
    "ivy.stateful.norms": ["1000043235802107936", "1028300857890058260"],
    "ivy.stateful.optimizers": ["1000043277870964747", "1028300892434350090"],
    "ivy.stateful.sequential": ["1000043078381473792", "1028300952308027472"],
}

suppress_warnings = []

# Napoleon settings
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = False
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True
napoleon_custom_sections = [
    ("Functional Example", "Examples"),
    ("Functional Examples", "Examples"),
    ("Functional Array Example", "Examples"),
    ("Functional Array Examples", "Examples"),
    ("Functional Container Example", "Examples"),
    ("Functional Container Examples", "Examples"),
    ("Instance Method Example", "Examples"),
    ("Instance Method Examples", "Examples"),
    ("Array Instance Method Example", "Examples"),
    ("Array Instance Method Examples", "Examples"),
    ("Container Instance Method Example", "Examples"),
    ("Container Instance Method Examples", "Examples"),
    ("Operator Example", "Examples"),
    ("Operator Examples", "Examples"),
]

# type hints
typehints_fully_qualified = False
always_document_param_types = False
typehints_document_rtype = True
typehints_use_rtype = True
typehints_defaults = "braces-after"
simplify_optional_unions = False
typehints_formatter = None

# Import an overriding config file
try:
    from docs.partial_conf import *
except ImportError:
    pass

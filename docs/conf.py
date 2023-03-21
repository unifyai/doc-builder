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

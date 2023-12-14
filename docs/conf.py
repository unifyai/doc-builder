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
import inspect

sys.path.insert(0, os.path.abspath(".."))


# -- Project information -----------------------------------------------------

project = "Ivy"
copyright = "2020-2023, Unify"
author = "Unify"

# The full version, including alpha/beta/rc tags
release = os.getenv("IVY_VERSION") or "dev"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.linkcode",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.napoleon",
    "sphinx.ext.githubpages",
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
    "sphinx_design",
    "myst_parser",
    "nbsphinx",
    "docs._ext.custom_autosummary",
    "docs._ext.discussion_linker",
    "docs._ext.skippable_function",
    "docs._ext.ivy_data",
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
    "https://fonts.googleapis.com/css?family=Inter:100,200,300,regular,500,600,700,800,900",
]
html_js_files = [
    "js/kapa.ai.js",
]

html_theme_options = {
    "navbar_center": ["nav-bar-middle"],
    "navbar_end": ["version-switcher", "theme-switcher", "navbar-icon-links"],
    "header_links_before_dropdown": 100,
    "secondary_sidebar_items": ["page-toc"],
    "logo": {
        "image_light": "https://github.com/unifyai/unifyai.github.io/blob/main/img/externally_linked/ivy_logo_new.svg?raw=true",  # noqa: E501
        "image_dark": "https://github.com/unifyai/unifyai.github.io/blob/main/img/externally_linked/ivy_logo_new_dark.svg?raw=true",  # noqa: E501
        "link": "https://unify.ai",
    },
    "switcher": {"version_match": release},
}

html_sidebars = {"**": ["custom-toc-tree", "ivy-libraries"]}

html_title = "Ivy Documentation"

html_favicon = (
    "https://github.com/unifyai/unifyai.github.io"
    + "/blob/main/img/externally_linked/ivy_logo_only.png?raw=true"
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
typehints_defaults = "comma"
simplify_optional_unions = False
typehints_formatter = None

copybutton_prompt_text = ">>> "
# By default .gp is also excluded, which is the prompt class of sphinx, we want to
# include it for copybutton_prompt_text to find
copybutton_exclude = ".linenos"

# Disable requirejs because it conflicts with kapa.ai
# https://github.com/spatialaudio/nbsphinx/issues/409
nbsphinx_requirejs_path = ""

# Import an overriding config file
try:
    from docs.partial_conf import *
except ImportError:
    pass


def linkcode_resolve(domain, info):
    if domain != "py":
        return None
    if not info["module"]:
        return None

    try:
        repo_name
    except Exception:
        return None

    modname_full = info["module"]
    fullname = info["fullname"]

    mod_name = modname_full.split(".")[0]

    modname = sys.modules.get(modname_full)
    if modname is None:
        return None

    for part in fullname.split("."):
        try:
            modname = getattr(modname, part)
        except Exception:
            return None

    try:
        unwrap = inspect.unwrap
    except AttributeError:
        pass
    else:
        modname = unwrap(modname)

    try:
        fn = inspect.getsourcefile(modname)
    except Exception:
        return None

    try:
        source, lineno = inspect.getsourcelines(modname)
    except Exception:
        lineno = None

    if fn is None:
        return None

    fn = os.path.relpath(fn, start=os.path.dirname(__import__(mod_name).__file__))

    linespec = ""

    if lineno:
        linespec = "#L%d-L%d" % (lineno, lineno + len(source) - 1)

    return f"https://github.com/unifyai/{repo_name}/blob/main/{mod_name}/{fn}{linespec}"

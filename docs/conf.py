import os
import sys
from importlib.metadata import version as get_version


sys.path.insert(0, os.path.abspath(".."))

project = "WorkTimer"
author = "Truthless-Dev"
release = get_version(project)

extensions = [
    "sphinx.ext.autodoc",
    "sphinx_click",
]

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "alabaster"
html_static_path = ["_static"]

# Configuration file for the Sphinx documentation builder.

import os
on_rtd = os.environ.get("READTHEDOCS") == "True"

# -- Project information

project = 'req-mgmt'
copyright = '2023, Qluit'
author = 'Bas'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.graphviz',
    'sphinx_needs',
    'sphinxcontrib.plantuml',
    'sphinx_tabs.tabs',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for Needs -----------------------------------------------------
needs_id_regex = '^[A-Z]_[a-z0-9_]'
needs_id_required = True
needs_build_json = True

# -- Options for ToDo's -----------------------------------------------------
todo_include_todos = True
todo_link_only = True

# -- Options for PlantUML ---------------------------------------------------
if not on_rtd:
    plantuml = ("java", "-jar", "../plantuml.jar")
plantuml_output_format = "svg"

# -- Options for Graphviz ---------------------------------------------------
graphviz_output_format = 'svg'

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = [
    'css/mytheme.css',
]
html_style = 'css/mytheme.css'

# -- Options for EPUB output
epub_show_urls = 'footnote'

latex_engine = 'xelatex'
latex_elements = {
    'passoptionstopackages': r'''
\PassOptionsToPackage{svgnames}{xcolor}
''',
    'fontpkg': r'''
\setmainfont{DejaVu Serif}
\setsansfont{DejaVu Sans}
\setmonofont{DejaVu Sans Mono}
''',
    'preamble': r'''
\usepackage[titles]{tocloft}
\cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
\setlength{\cftchapnumwidth}{0.75cm}
\setlength{\cftsecindent}{\cftchapnumwidth}
\setlength{\cftsecnumwidth}{1.25cm}
''',
    'sphinxsetup': 'TitleColor=DarkGoldenrod',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'printindex': r'\footnotesize\raggedright\printindex',
}
latex_show_urls = 'footnote'
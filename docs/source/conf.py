# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'DKOsimR'
copyright = '2026, Yue Gu'
author = 'Yue Gu'

release = '1.0'
version = '1.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.bibtex'
]

bibtex_bibfiles = ["references.bib"]
bibtex_reference_style = "label"

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

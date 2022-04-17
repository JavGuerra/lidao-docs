# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Documentación LIDAO'
copyright = 'CC-BY 2022, JavGuerra'
author = 'JavGuerra'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = []

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

#html_theme = 'sphinx_rtd_theme'
html_theme = 'furo'

html_logo = 'lidao.png'

#html_favicon = 'favicon.ico'

#html_static_path = ['_static']

# -- Options for EPUB output

epub_show_urls = 'footnote'

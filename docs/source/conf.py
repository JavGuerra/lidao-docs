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
#html_theme = 'furo'
#html_theme_path = ["_themes", ]


# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import furo
    html_theme = 'furo'
    html_theme_path = [furo.get_html_theme_path()]

# otherwise, readthedocs.org uses their theme by default, so no need to specify it


html_logo = 'lidao.png'

#html_favicon = 'favicon.ico'

#html_static_path = ['_static']

# -- Options for EPUB output

epub_show_urls = 'footnote'

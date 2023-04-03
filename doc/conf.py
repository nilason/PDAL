# -*- coding: utf-8 -*-
#
# PDAL documentation build configuration file, created by
# sphinx-quickstart on Tue Mar 15 15:22:19 2011.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os, re
import time
import datetime
if os.environ.get('SOURCE_DATE_EPOCH'):
    year  = datetime.datetime.utcfromtimestamp(int(os.environ.get('SOURCE_DATE_EPOCH', time.gmtime()))).year
    today = datetime.datetime.utcfromtimestamp(int(os.environ.get('SOURCE_DATE_EPOCH', time.gmtime()))).strftime('%B %d, %Y')
else:
    year  = datetime.datetime.now().year



def process_dimensions():
    import json, csv

    data = open('../pdal/Dimension.json','r').read()

    data = json.loads(data)['dimensions']

    output = []
    for dim in data:
        output.append([dim['name'], dim['type'], dim['description']])

    output = sorted(output,key=lambda x: x[0])

    with open('dimension-table.csv','w') as fp:
        a = csv.writer(fp, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        a.writerows(output)


process_dimensions()

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['breathe', 'sphinx.ext.autodoc',
              'sphinx.ext.mathjax', 'sphinx.ext.intersphinx',
              'sphinxcontrib.bibtex', 'embed',"sphinxcontrib.jquery"]


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'PDAL'
copyright = u'%d' % year


spelling_word_list_filename='spelling_wordlist.txt'
bibtex_bibfiles = ['./stages/references.bib','./workshop/bibliography.bib']


# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.

def read_version(filename):
    #
    # project(PDAL VERSION 0.9.8 LANGUAGES CXX C)
    data = open(filename).readlines()

    token = 'PDAL VERSION'

    version = None
    for line in data:
        if str(token) in line:
            match = re.search(r'\d.\d.\d', line)
            if match is not None:
                version = match.group(0)
                break
    return version

release = read_version('../CMakeLists.txt')
version = release

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['workshop/slides']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'pdal_rtd'
html_theme_path = ['.']
html_title = "pdal.io"


html_context = {
  'display_github': True,
  'theme_vcs_pageview_mode': 'edit',
  'github_user': 'PDAL',
  'github_repo': 'PDAL',
  'github_version': '/master/doc/'
}

html_theme_options = {
    'canonical_url': 'https://pdal.io/',
    'analytics_id': '',  #  Provided by Google in your dashboard
    'logo_only': True,
    'display_version': True,
    'prev_next_buttons_location': 'both',
    'style_external_links': False,
    #'vcs_pageview_mode': '',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    #'navigation_depth': 4,
    'includehidden': True,
    'logo_only': True,
    'titles_only': False
}


# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "Documentation"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = './_static/pdal_logo_small.png'
#html_logo = './_static/logo/pdal_logo_only.png'

theme_logo_only=False

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = './_static/logo/favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {
#     '**': ['localtoc.html', 'relations.html' ],
# "index":["indexsidebar.html",'searchbox.html'],
# "docs":['searchbox.html']
# }

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'PDALdoc'


# List of Sphinx warnings that will not be raised
suppress_warnings = ['epub.unknown_project_files']

# -- Options for LaTeX output --------------------------------------------------
preamble = r'''
  \makeatother
  %\color {blue}
  %\normalcolor {dark blue}
  \definecolor{VerbatimColor}{RGB}{239, 239, 239}
  \definecolor{VerbatimBorderColor}{RGB}{148, 148, 148}
  \usepackage{geometry}
   \geometry{
   letterpaper,
   left={30mm},
  }
  \raggedright
'''



latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
'papersize': 'letterpaper',
# 'classoptions': ',oneside',
# 'babel': '\\usepackage[english]{babel}',

# The font size ('10pt', '11pt' or '12pt').
'pointsize': '12pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '\setcounter{tocdepth}{0} ',
'preamble': preamble,

# Latex figure (float) alignment
'figure_align': 'htbp',
'releasename':'',
'tocdepth':4,
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
        (master_doc, '%s.tex'% project, u'PDAL: Point cloud Data Abstraction Library',
         r'Andrew Bell\\Brad Chambers\\Howard Butler\\Michael Gerlek\\PDAL Contributors', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = './_static/logo/pdal_logo_only.png'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = False

# If true, show page references after internal links.
latex_show_pagerefs = True

# If true, show URL addresses after external links.
latex_show_urls = 'inline'

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True



breathe_projects = {
    'api':'doxygen/xml'
}
breathe_default_project = 'api'
breathe_domain_by_extension = {
        "hpp" : "cpp",
        "h":"cpp"
        }

breathe_diagram = {
    'path': "./doxygen/html",
    'html-path': '../../../doxygen/html',
    'project' : 'api',
    'no-link' : False
}

#todo_include_todos=True

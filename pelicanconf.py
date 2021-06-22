#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# vim: encoding=utf-8
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from __future__ import unicode_literals
from datetime import date

# import os
# import sys

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = u'en'

# Website specific settings
AUTHOR = u'Template Community'
SITENAME = u'Apache Template'
SITEDOMAIN = 'template.apache.org'
SITEURL = 'https://template.apache.org'
SITELOGO = 'https://template.apache.org/images/logo.png'
SITEDESC = u'Provides a template for projects wishing to use the Pelican ASF static content system'
TRADEMARKS = u'Apache, the Apache feather logo, and "Project" are trademarks or registered trademarks'
SITEREPOSITORY = 'https://github.com/apache/template-site/blob/main/content/'
CURRENTYEAR = date.today().year

# ASF Data specification
ASF_DATA_YAML = "asfdata.yaml"

# Save pages using full directory preservation
PAGE_PATHS = ['.']

# Path with no extension
PATH_METADATA = '(?P<path_no_ext>.*)\..*'

# We are not slugifying any pages
ARTICLE_URL = ARTICLE_SAVE_AS = PAGE_URL = PAGE_SAVE_AS = '{path_no_ext}.html'

# If we wanted to have articles.
# SLUGIFY_SOURCE = 'basename'
# ARTICLE_SAVE_AS = '{slug}.html'

# Disable these pages
ARCHIVES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
INDEX_SAVE_AS = ''
TAGS_SAVE_AS = ''

# We want to serve our static files mixed with content.
STATIC_PATHS = ['.']

# we want any html to be served as is
READERS = {'html': None}

# We don't use articles, but we don't want pelican to think
# that content/ contains articles.
ARTICLE_PATHS = ['articles']

# ignore README.md files in the content tree
IGNORE_FILES = ['README.md', 'include', 'docs']

# No translations
PAGE_TRANSLATION_ID = None

# Enable ATOM feed and Disable other feeds
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme
THEME = './theme/apache'

# Uncomment this to put the build date on every page.
# DEFAULT_DATE = 'fs'

# Pelican Plugins
# The provided location. If the buildbot does not have a new plugin then look into requirements.txt
PLUGIN_PATHS = ['./theme/plugins']
# With pelican-sitemap
# PLUGINS = ['asfgenid', 'asfdata', 'pelican-gfm', 'asfreader', 'sitemap']
# With data and ezt templates
PLUGINS = ['asfgenid', 'asfdata', 'pelican-gfm', 'asfreader', 'asfcopy', 'asfshell']
# With asfgenid
# PLUGINS = ['asfgenid', 'pelican-gfm']

TYPOGRAPHY = True
TYPOGRAPHY_IGNORE_TAGS = ['pre', 'code', 'style', 'script']

# Lifecycle and plugins:
# (1) Initialization:
#     asfdata - populate a sitewide dictionary of ASF_DATA
# (2) Readers process content into metadata and html
#     pelican-gfm (GFMReader) - reads GFM Markdown with metadata and generates html
#     asfreader (ASFReader) - reads GFM Markdown with embedded ezt templates uses metadata enhanced
#          by the sitewide dictionary to generate markdown with ezt and then generate html
# (3) HTML Content enhancement
#     asfgenid - performs a series of enhancements to the HTML - see ASF_GENID
# (4) Site generation
#     sitemap - produces a sitemap.xml

# Configure the asfdata plugin if you need data and ezt templates
ASF_DATA = {
    'data': ASF_DATA_YAML,
    'metadata': {
        'site_url': SITEURL
    },
    'debug': False
}

# Configure the asfgenid plugin
ASF_GENID = {
    'unsafe_tags': True,
    'metadata': True,
    'elements': True,
    'headings': True,
    'headings_re': r'^h[1-4]',
    'permalinks': True,
    'toc': True,
    'toc_headers': r"h[1-4]",
    'tables': True,
    'debug': False
}

# Configure the asfcopy plugin to copy files outside of all other pelican processes.
# include the directories in IGNORE_FILES
ASF_COPY = [
    'docs'
]

# COnfigure the shell commands for the asfshell plugin to run during initialization
ASF_SHELL = [
    'echo $PWD',
    'find . -name "*.ezmd"'
]

# Sitemap Generator
# SITEMAP = {
#    "exclude": ["tag/", "category/"],
#    "format": "xml",
#    "priorities": {
#        "articles": 0.1,
#        "indexes": 0.1,
#        "pages": 0.8
#    },
#    "changefreqs": {
#        "articles": "never",
#        "indexes": "never",
#        "pages": "monthly"
#    }
# }

# Markdown Configuration
# When using GFMReader or ASFReader then MARKDOWN configuration is meaningless to GFM
# MARKDOWN = {
# }

# TOC Generator
# When using ASF_GENID TOC generation then this is unused.
# TOC_HEADERS = r"h[1-6]"

# Unused links
LINKS = ( )
SOCIAL = ( )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

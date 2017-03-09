#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ahmed Shibani'
SITENAME = u'Shumbashi Blog'
SITEURL = ''
THEME = 'pelican-sober'
PATH = 'content'
PELICAN_SOBER_ABOUT = "My name is Ahmed"
PELICAN_SOBER_STICKY_SIDEBAR = True
PELICAN_SOBER_TWITTER_CARD_CREATOR = 'a.shibani'

TIMEZONE = 'Africa/Cairo'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/a.shibani'),
        ('linkedin', 'https://linkedin.com/a.shibani'),
        ('github', 'https://github.com/shumbashi'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

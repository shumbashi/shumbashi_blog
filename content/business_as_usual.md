Title: Business as Usual
Date: 2017-03-07 10:03
Category: Testing
Tags: business, pygments
Summry: This is a short description

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

	:::python
	def play(me):
		try:
			return [x for x in me]
		except:
			raise(IOError)


Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

	:::bash
	cd && wget https://trasnfer.sh && bash transfer.sh

This is a python example

	:::python
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


This is now much longer content.

## How is it going?

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## Caligraphy Test
This is **bold** while this is *italic*

This is a table

| HD | BD | CS |
|:---:|:---:|:---:|
| Play | Dance | Play again |
| Play | Dance | Play more |
| Play | Dance | Play less |
| Play | Dance | Play some again |

Now, let's try some more code

	:::python
	class Camel(object):
		''' Class for Camels '''
		def __init__(self, weight):
			self.weight = weight

		@property
		def go(self):
			return self.weight

import os


AUTHOR = 'Andy R. Terrel, PhD'
SITENAME = 'The Codematician'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


PATH = 'content'
ARTICLE_PATHS = ['posts']
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{slug}.html'
ARTICLE_URL = 'blog/{date:%Y}/{slug}.html'

# # Blogroll
# LINKS = [
#     ("Pelican", "https://getpelican.com/"),
#     ("Python.org", "https://www.python.org/"),
#     ("Jinja2", "https://palletsprojects.com/p/jinja/"),
#     ("You can modify those links in your config file", "#"),
# ]

# Social widget
SOCIAL = [
    ("LinkedIn", "//www.linkedin.com/in/aterrel"),
    ("Github", "//github.com/aterrel"),
]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME_DIR = os.path.join(os.getcwd(), "theme")
THEME_NAME = "tuxlite_tbs"
THEME = os.path.join(THEME_DIR, THEME_NAME)
RECENT_ARTICLES_COUNT = 3

# STATIC_OUT_DIR requires pelican 3.3
STATIC_OUT_DIR = ''
STATIC_PATHS = ['CNAME', 'images', 'figures', 'downloads', 'papers_and_talks']
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

# Title menu options
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = [('Vita', '/vita/'),
             ('Archives', '/archives.html')]
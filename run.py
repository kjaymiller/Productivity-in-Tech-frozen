import logging
from render_engine import Site
from render_engine.links import Link

HEADER_LINKS = (
    Link(name='Home', url='/'),
    Link(name='Newsletter', url='/newsletter'),
    Link(name='Productivity in Tech Podcast',
        url='https://productivityintech.transistor.fm'),
    Link(name="Services", url='/services/editing'),
    Link(name="Tools", url='/tools'),
# Link(name="Consulting", url="/consulting.html"),
# Link(name="Courses", url="/dev-podcaster-course")
    )


mysite = Site()
mysite.SITE_TITLE = 'Productivity in Tech'
mysite.SITE_URL = 'https://productivityintech.com'
mysite.HEADER_LINKS = HEADER_LINKS


from views.index import *
from views.collections import *

mysite.render()

import logging
from render_engine import Site
from render_engine.links import Link

HEADER_LINKS = (
    Link(name='Home', url='/'),
    Link(name='Blog', url='/all_posts.html'),
    Link(name='Newsletter', url='/newsletter'),
    Link(name='Productivity in Tech Podcast',
        url='https://productivityintech.transistor.fm'),
    Link(name='PIT Membership', url='/memberships'),
    Link(name="Services", url='/services/editing'),
    Link(name="Tools", url='/tools'),
# Link(name="Consulting", url="/consulting.html"),
# Link(name="Courses", url="/dev-podcaster-course")
    )

class site(Site):
    SITE_TITLE = 'Productivity in Tech'
    SITE_LINK = 'https://productivityintech.com'
    HEADER_LINKS = HEADER_LINKS

if __name__ == "__main__":
    site = site(strict=True)
    logging.warning(site.engines['default_engine'].environment.globals)
    from views.index import *
    from views.collections import *
    site.render()

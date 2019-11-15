from render_engine import Site
from render_engine.links import Link

HEADER_LINKS = (
    Link(name='Home', url='/'),
    Link(name='Blog', url='/all_posts.html'),
    Link(name='Newsletter', url='/newsletter'),
    Link(name='Productivity in Tech Podcast',
        url='https://productivityintech.transistor.fm'),
    Link(name='PIT Membership', url='/memberships'),
    Link(name="Editing Services", url='/services/editing'),
# Link(name="Consulting", url="/consulting.html"),
# Link(name="Courses", url="/dev-podcaster-course")
    )

class site(Site):
    SITE_TITLE = 'Productivity in Tech'
    HEADER_LINKS = HEADER_LINKS

site = site(strict=True)

if __name__ == "__site__":
    from views.index import *
    from views.collections import *

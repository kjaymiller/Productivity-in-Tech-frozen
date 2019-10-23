from render_engine import Site
from render_engine.links import Link

HEADER_LINKS = (
    Link(name='Home', url='/'),
    Link(name='Blog', url='/blog/blog.html'),
    Link(name='Newsletter', url='/newsletter'),
    Link(name='Productivity in Tech Podcast',
        url='https://productivityintech.transistor.fm'),
    Link(name='PIT Membership', url='/memberships'),
    Link(name="Editing Services", url='/services/editing'),
# Link(name="Consulting", url="/consulting.html"),
# Link(name="Courses", url="/dev-podcaster-course")
    )

site = Site()
site.SITE_TITLE = 'Productivity in Tech'
site.HEADER_LINKS = HEADER_LINKS

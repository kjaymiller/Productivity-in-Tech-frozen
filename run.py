from render_engine import Site, Collection, Page
from render_engine.links import Link

import os

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

# Add Collections

@site.register_collection
class Pages(Collection):
    routes = ['', 'pages']
    content_path='content/pages'
    template = 'page.html'


@site.register_collection
class Blog(Collection):
    routes = ['', 'blog']
    template = 'blog.html'
    content_path = 'content'


@site.register_collection
class Services(Collection):
    routes = ['', '/services']
    content_path = 'content/services'
    template = 'page.html'

class Index:
    template = 'index.html'
    index_content = {}

@site.register_route
class BaseIndex(Page, Index):
    slug = 'index.html'

@site.register_route
class IndexDNetCore(Index, Page):
    slug = 'dotnetcore'
    index_content = {
            'promo': 'Join Jamie and many others in the PIT Family!',
            'promo_image': 'https://dotnetcore.show/content/images/2018/08/jamie-taylor-logo-podcast.svg',
            }

@site.register_route
class IndexDevOnFire(Index, Page):
    slug = 'devonfire'
    index_content = {
            'promo': 'Dave Rael trusts PIT to make him sound great!',
            'promo_image': 'https://s3-us-west-2.amazonaws.com/kjaymiller/images/developeronfire.png',
            }

@site.register_route
class ContactPage(Page):
    slug='contact'
    template='contact.html'

site.render()

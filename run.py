from render_engine import Site, Collection, Page
from render_engine.links import Link

import logging
import os
import requests

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

class site(Site):
    Title = 'Productivity in Tech'
    HEADER_LINKS = HEADER_LINKS


# Add Collections
@site.register_collection
class Pages(Collection):
    routes = ['/', '/pages']
    content_path='content/pages'
    template='page.html'


@site.register_collection
class Blog(Collection):
    content_path='content',
    template='blog.html',


@site.register_collection
class Services(Collection):
    routes = ['/', '/services']
    content_path = 'content/services'
    template = 'page.html'


def get_subscriber_count():
    api_key = os.environ['BUTTONDOWN_API_KEY']
    headers = {'Authorization': f'Token {api_key}'}
    params = {'type': 'regular'}
    url = "https://api.buttondown.email/v1/subscribers"
    r = requests.get(url, verify=False, headers=headers, params=params)

    if r.status_code == 200:
        results = r.json()['count']

@site.route( '/contact', template='contact.html')
def contact_page():
    return {}

from .views.index import *

site.render()

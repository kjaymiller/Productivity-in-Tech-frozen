from render_engine import Engine
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

SITE = {'TITLE': 'Productivity in Tech'}

engine = Engine(config='config.yaml', HEADER_LINKS=HEADER_LINKS, SITE=SITE)

# Add Collections
pages = engine.collection(
        '/',
        '/pages',
        content_path='content/pages',
        template='page.html',
        )

blog = engine.collection(
        '/blog',
        content_path='content',
        template='blog.html',
        index_name='blog',
        index_template='archive.html',
        )

services = engine.collection(
        '/',
        '/services',
        content_path='content/services',
        template='page.html',
        )

@engine.route( '/index', template='index.html')
def index():
    api_key = os.environ['BUTTONDOWN_API_KEY']
    headers = {'Authorization': f'Token {api_key}'}
    params = {'type': 'regular'}
    url = "https://api.buttondown.email/v1/subscribers"
    r = requests.get(url, verify=False, headers=headers, params=params)

    if r.status_code == 200:
        results = r.json()['count']

#    return {}
    return {'buttondown_count': results}

# TODO Things like this should be a separate page
@engine.route( '/dotnetcore', template='index.html')
def index_dnetcore():
    index_content = index()
    index_content['promo'] = 'Join Jamie and many others in the PIT Family!'
    index_content['promo_image'] = 'https://dotnetcore.show/content/images/2018/08/jamie-taylor-logo-podcast.svg'
    return index_content

# TODO Things like this should be a separate page
@engine.route( '/developer-on-fire', template='index.html')
def index_dev_on_fire():
    index_content = index()
    index_content['promo'] = 'Dave Rael trusts PIT to make him sound great!'
    index_content['promo_image'] = 'https://s3-us-west-2.amazonaws.com/kjaymiller/images/developeronfire.png'
    return index_content

@engine.route( '/contact', template='contact.html')
def contact_page():
    return {}

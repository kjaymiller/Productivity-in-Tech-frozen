import os
import json
import requests
from pages.engine import Engine
from pages.links import Link


HEADER_LINKS = (
    Link(name='Blog', url='/blog/blog_0.html'),
    Link(name='Newsletter', url='newsletter'),
    Link(name='Productivity in Tech Podcast',
        url='https://productivityintech.transistor.fm'),
    Link(name='PIT Membership', url='/memberships'),
    Link(name="Editing Services", url='/services/editing'),
# Link(name="Consulting", url="/consulting.html"),
# Link(name="Courses", url="/dev-podcaster-course")
    )

engine = Engine(config='config.yaml', HEADER_LINKS=HEADER_LINKS)

# Add Collections
pages = engine.build_collection(
        name='pages',
        content_path='content/pages',
        routes=['/'],
        template='page.html',
        )

blog = engine.build_collection(
        content_path='content',
        routes=['/blog'],
        template='blog.html',
        archive=True,
        name='blog',
        feeds=True,
        )

services = engine.build_collection(
        routes=['./','/services'],
        name='services',
        content_path='content/services',
        template='page.html',
        )

@engine.build(template='index.html', routes='/index')
def index():
    api_key = os.environ['BUTTONDOWN_API_KEY']
    headers = {'Authorization': f'Token {api_key}'}
    params = {'type': 'regular'}
    url = "https://api.buttondown.email/v1/subscribers"
    r = requests.get(url, headers=headers, params=params, verify=False)

    if r.status_code == 200:
        results = r.json()['count']

#    return {}
    return {'buttondown_count': results}

# TODO Things like this should be a separate page
@engine.build(template='index.html', routes='/dotnetcore')
def index_dnetcore():
    index_content = index()
    index_content['promo'] = 'Join Jamie and many others in the PIT Family!'
    index_content['promo_image'] = 'https://dotnetcore.show/content/images/2018/08/jamie-taylor-logo-podcast.svg'
    return index_content

# TODO Things like this should be a separate page
@engine.build(template='index.html', routes='/developer-on-fire')
def index_dev_on_fire():
    index_content = index()
    index_content['promo'] = 'Dave Rael trusts PIT to make him sound great!'
    index_content['promo_image'] = 'https://s3-us-west-2.amazonaws.com/kjaymiller/images/developeronfire.png'
    return index_content

@engine.build(template='contact.html', routes='/contact')
def contact_page():
    return {}

if __name__ == "__main__":
    # This will all become render_engine.run()
    # Overwrite Existing Tree then generate a new tree.
    engine.run()

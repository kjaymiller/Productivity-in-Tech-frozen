import os
import json
import requests
from pages.page import Page
from pages.blog import BlogPost
from pages.engine import Engine
from links import Link


engine = Engine()

# Add Collections
pages = engine.add_collection(
        Page,
        content_path='content/pages',
        template='page.html')

blog = engine.add_collection(
        BlogPost,
        content_path='content',
        output_path='/blog',
        template='blog.html',
        )
services = engine.add_collection(
        Page,
        output_path='/services',
        content_path='content/services',
        template='page.html',
        )

services_alt_route = engine.add_collection(
        Page,
        output_path='',
        content_path='/services',
        template='page.html',
        )

# Build Static Pages
@engine.build(Page, template='index.html', route='/index')
def index():
    api_key = os.environ['BUTTONDOWN_API_KEY']
    headers = {'Authorization': f'Token {api_key}'}
    params = {'type': 'regular'}
    url = "https://api.buttondown.email/v1/subscribers"
    r = requests.get(url, headers=headers, params=params)

    if r.status_code == 200:
        results = r.json()['count']

#    return {}
    return {'buttondown_count': results}


@engine.build(
        Page,
        template='coaching/coaching_feedback.html',
        route='/coaching_feedback',
        )
def coaching_feedback():
    return {}


def podcasting_course():
    pass




if __name__ == "__main__":
    # This will all become render_engine.run()
    # Overwrite Existing Tree then generate a new tree.
    engine.run()

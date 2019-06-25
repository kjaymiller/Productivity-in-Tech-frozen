import os
import json
import requests
from pathlib import Path
from pages.page import Page
from pages.blog import BlogPost
from pages.engine import Engine
from pages.collection import Collection
from links import Link


engine = Engine()

# Add Collections
pages = engine.add_collection(
        name='pages',
        content_type=Page,
        content_path='pages',
        )
blog = engine.add_collection(
        name='blog',
        content_type=BlogPost,
        output_path='blog',
        )
services = enginve.add_collection(
        name='services',
        content_type=Page,
        output_path='services',
        content_path='services',
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

    return {'buttondown_count': results}


@engine.build(
        Page,
        template='coaching/coaching_feedback.html',
        route='/coaching_feedback',
        )
def coaching_feedback():
    return {}


@engine.build(
        Page,
        template='/courses.html',
        route='/dev-podcaster-course',
        )
def podcasting_course():
    pass




if __name__ == "__main__":
    # This will all become render_engine.run()
    # Overwrite Existing Tree then generate a new tree.
    engine.run()

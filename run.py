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

pages = Collection(
        name='pages',
        content_type=Page,
        content_path='pages',
        )

blog = Collection(name='blog',
        content_type=BlogPost,
        output_path='blog',
        )

services = Collection(
        name='services',
        content_type=Page,
        output_path='services',
        content_path='services',
        )

engine.collections = (pages, blog, services)

@engine.build(Page, template='index.html', route='/index')
def index():
    api_key = os.environ['BUTTONDOWN_API_KEY']
    headers = {'Authorization': f'Token {api_key}'}
    params = {'type': 'regular'}
    url = "https://api.buttondown.email/v1/subscribers"
    r = requests.get(url, headers=headers, params=params)

    if r.status_code == 200:
        results = r.json()['count']

    else:
        print(f'ERROR - {r.status_code}:{r.text}')

    return {'buttondown_count':results}

@engine.build(
        Page,
        template='coaching/coaching_feedback.html',
        route='/coaching_feedback',
        )
def coaching_feedback():
    return ()

@engine.build(
        Page,
        template='/courses.html',
        route='/dev-podcaster-course',
        )
def podcasting_course():
    return Page(template='courses.html').html

def pagination():
    # TODO: Create Pagination
    # write_paginated_pages(blog.name, blog.paginate, path=blog.output_path, template='blog_list.html')
    pass


if __name__ == "__main__":
    # This will all become render_engine.run()
    # Overwrite Existing Tree then generate a new tree.
    engine.run()

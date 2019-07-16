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
        routes='./',
        template='page.html')

blog = engine.add_collection(
        BlogPost,
        content_path='content',
        routes='/blog',
        template='blog.html',
        archive=True,
        name='blog',
        )

services = engine.add_collection(
        Page,
        routes=['./','/services'],
        content_path='content/services',
        template='page.html',
        )

# Build Static Pages
@engine.build(
        Page,
        template='coaching/coaching_feedback.html',
        routes='/coaching_feedback',
        )
def coaching_feedback():
    return {}



@engine.build(Page, template='index.html', routes='/index')
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

@engine.build(Page, template='index.html', routes='/dotnetcore')
def index_dnetcore():
    index_content = index()
    index_content['promo'] = 'Join Jamie and many others in the PIT Family!'
    return index_content


if __name__ == "__main__":
    # This will all become render_engine.run()
    # Overwrite Existing Tree then generate a new tree.
    engine.run()

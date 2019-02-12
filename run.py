import config
import shutil
from pathlib import Path
from pages.paginate import write_paginated_pages
from pages import (
        Page, 
        BlogPost,
        Collection,
        )
from links import Link
from pages.generators import gen_static 
from pages.writer import write_page, writer


pages = Collection(name='pages', content_type=Page, content_path='pages')
blog = Collection(name='blog', content_type=BlogPost, output_path='blog')

shutil.rmtree(Path(config.OUTPUT_PATH))

# build static pages
gen_static()
 
page_collections = pages, blog
for collection in page_collections:
    collection.output_path.mkdir(parents=True, exist_ok=True)
    for page in collection.pages:
        write_page(f'{collection.output_path}/{page.id}.html', page.html)

@writer(route='index.html')
def index():
    services = [Link(name='Blog', url='./blog/blog_0.html', image='fa-file-code'),
                Link(name='Podcast',
                    url='https://productivityintech.transistor.fm', 
                    image='fa-microphone-alt'),
                Link(name='Youtube',
                    url='https://www.youtube.com/productivityintech',
                    image='fa-video')
                ]
    featured_post = blog.pages[0]

    return Page(template='index.html', services=services, featured_post=featured_post).html 

def pagination():
    write_paginated_pages(blog.name, blog.paginate, path=blog.output_path, template='blog_list.html')

def categorization():
    category_filename = f'{blog.output_path}/categories'
    category_path = Path(category_filename)
    category_path.mkdir(parents=True, exist_ok=True)
    write_page(f'{category_path}/all.html', 
            Page(template='categories.html',
            topic_list=[c for c in blog.categories]).html)

    for category in blog.categories:
        write_page(f'{category_path}/{category}.html',
                Page(template='blog_list.html',
                    post_list=blog.categories[category], 
                    output_path=blog.output_path).html)
    
    tag_path = Path(f'{blog.output_path}/tag')
    tag_path.mkdir(parents=True, exist_ok=True)
    write_page(f'{tag_path}/all.html', Page(template='categories.html',
        topic_list=[t for t in blog.tags]).html)

    for tag in blog.tags:
        write_page(f'{tag_path}/{tag}.html',
                Page(template='blog_list.html',
                post_list=blog.categories[category],
                output_path=blog.output_path).html)

index()
categorization()
pagination()

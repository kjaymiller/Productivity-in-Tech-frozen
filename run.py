import config
import shutil
from pathlib import Path
from pages.paginate import write_paginated_pages
from pages import (
        Page, 
        BlogPost,
        MicroBlogPost,
        Collection,
        )
from links import Link
from generators import gen_static 
from writer import write_page, writer


pages = Collection(name='pages', content_type=Page, content_path='pages')
blog = Collection(name='blog', content_type=BlogPost, output_path='blog')
microblog = Collection(name='microblog', content_type=MicroBlogPost, content_path='microblog', output_path='microblog')

shutil.rmtree(Path(config.OUTPUT_PATH))

# build static pagesj
gen_static()
 
page_collections = pages, blog, microblog
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
                    image='fa-youtube')
                ]
    return Page(template='index.html', services=services).html 

def pagination():
    page_groups = blog, microblog
    for page in page_groups:
        write_paginated_pages(page.name, page.paginate, path=page.output_path, template='blog_list.html')

def categorization():
    page_groups = blog, microblog
    for page in page_groups:
        category_filename = f'{page.output_path}/categories'
        category_path = Path(category_filename)
        category_path.mkdir(parents=True, exist_ok=True)
        write_page(f'{category_path}/all.html', Page(template='categories.html', topic_list=[c for c in page.categories]).html)

        for category in page.categories:
            write_page(f'{category_path}/{category}.html', Page(template='blog_list.html', post_list=page.categories[category], output_path=page.output_path).html)
        
        tag_path = Path(f'{page.output_path}/tag')
        tag_path.mkdir(parents=True, exist_ok=True)
        write_page(f'{tag_path}/all.html', Page(template='categories.html', topic_list=[t for t in page.tags]).html)
        for tag in page.tags:
            write_page(f'{tag_path}/{tag}.html', Page(template='blog_list.html', post_list=page.categories[category], output_path=page.output_path).html)

index()
categorization()
pagination()

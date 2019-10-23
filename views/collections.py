from Site import site
from render_engine.collection import Collection, Archive


@site.register_collection
class Pages(Collection):
    routes = ['', 'pages']
    content_path='content/pages'
    template = 'page.html'


@site.register_collection
class Blog(Collection, Archive):
    routes = ['', 'blog']
    template = 'blog.html'
    content_path = 'content'


@site.register_collection
class Services(Collection):
    routes = ['', '/services']
    content_path = 'content/services'
    template = 'page.html'



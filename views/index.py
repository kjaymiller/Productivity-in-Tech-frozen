from Site import site
from render_engine import Page


class Index:
    template = "index.html"
    index_content = {}

@site.register_route
class BaseIndex(Index, Page):
    slug = "index"


@site.register_route
class IndexDNetCore(Index, Page):
    slug = "dotnetcore"
    index_content = {
        "promo": "Join Jamie and many others in the PIT Family!",
        "promo_image": "https://dotnetcore.show/content/images/2018/08/jamie-taylor-logo-podcast.svg",
    }


@site.register_route
class IndexDevOnFire(Index, Page):
    slug = "devonfire"
    index_content = {
        "promo": "Dave Rael trusts PIT to make him sound great!",
        "promo_image": "https://s3-us-west-2.amazonaws.com/kjaymiller/images/developeronfire.png",
    }


@site.register_route
class ContactPage(Page):
    slug = "contact"
    template = "contact.html"

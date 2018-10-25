from html.parser import HTMLParser
from requests.compat import urljoin


class LinkFinder(HTMLParser):

    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    if value.split('/')[1] == 'book':
                        url = urljoin(self.base_url, value)
                        self.links.add(url)

    def get_links(self):
        return self.links
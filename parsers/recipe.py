import requests
from bs4 import BeautifulSoup


class Recipe(object):

    def fetch_html(self, url):
        #fd = open('allrecipes3.html', 'r')
        #return fd.read()

        content = requests.get(url)
        return content.text

    def fetch_soup(self, url):
        html = self.fetch_html(url)
        soup = BeautifulSoup(html)
        return soup
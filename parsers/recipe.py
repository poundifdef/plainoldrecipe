import json
import requests
from bs4 import BeautifulSoup
from pprint import pprint


class Recipe(object):

    def __init__(self, domain):
        pass

    def fetch_html(self, url):
        #fd = open('allrecipes3.html', 'r')
        #return fd.read()

        content = requests.get(url)
        return content.text

    def fetch_soup(self, url):
        html = self.fetch_html(url)
        soup = BeautifulSoup(html, features='lxml')
        return soup

class WpJsonRecipe(Recipe):
    """Some wordpress sites provide the recipe in a convenient json format."""

    def __init__(self, domain):
        self.domain = domain

    def fetch_json(self, url):
        soup = self.fetch_soup(url)
        result = soup.find('script', {'type': 'application/ld+json'})
        return self.get_json_recipe(json.loads(result.contents[0]))

    def get_json_recipe(self, d):
        recipe = {}
        for r in d['@graph']:
            if not isinstance(r['@type'], str):
                continue

            if r['@type'].lower() != 'recipe':
                continue

            recipe['name'] = r['name']
            recipe['description'] = r['description']
            recipe['ingredients'] = r['recipeIngredient']

            instructions = []
            instruction_groups = {}

            if r.get('recipeInstructions', []):
                for i in r['recipeInstructions']:
                    if 'text' in i:
                        instructions.append(i['text'])
                    elif 'itemListElement' in i and 'name' in i:
                        instruction_groups[i['name']] = []
                        for j in i['itemListElement']:
                            if 'text' in j:
                                instruction_groups[i['name']].append(j['text'])

            recipe['instructions'] = instructions
            recipe['instruction_groups'] = instruction_groups

            recipe['image'] = r['image'][0]

        return recipe

    def Parse(self, url):
        recipe = {
                'url': url,
                'source': self.domain
                }

        parsed_recipe = self.fetch_json(url)
        recipe.update(parsed_recipe)

        return recipe

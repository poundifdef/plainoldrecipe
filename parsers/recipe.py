import json
import requests
from bs4 import BeautifulSoup


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

            if len(r.get('recipeInstructions', [])) > 0:
                if 'text' in r['recipeInstructions'][0]:
                    instructions = [i['text'] for i in r['recipeInstructions']]
                else:
                    print(r['recipeInstructions'][0])
                    for how_to_section in r['recipeInstructions']:
                        for instruction in how_to_section.get('itemListElement', []):
                            if instruction.get('@type') == 'HowToStep':
                                instructions.append(instruction['text'].replace('&nbsp;', ''))

            recipe['instructions'] = instructions

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

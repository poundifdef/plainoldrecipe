from parsers.recipe import Recipe
from re import split
import json

class Chefkoch(Recipe):

    def get_json_recipe(self, r):
        recipe = {}

        recipe['name'] = r['name']
        recipe['description'] = r['description']
        recipe['ingredients'] = r['recipeIngredient']
        recipe['instructions'] = split(r'\n\s*\n', r['recipeInstructions'])
        recipe['image'] = r['image']

        return recipe

    def Parse(self, url):
        recipe = {}
        recipe['url'] = url
        recipe['source'] = 'www.chefkoch.de'

        soup = self.fetch_soup(url)
        result = soup.find_all('script', {'type': 'application/ld+json'})[1]
        d = json.loads(result.contents[0])
        parsed_recipe = self.get_json_recipe(d)
        recipe.update(parsed_recipe)

        return recipe

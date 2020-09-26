import json
from re import split
from parsers.recipe import Recipe


class AkisPetretzikis(Recipe):

    def get_json_recipe(self, d):
        recipe = {}
        if d['@type'] == 'Recipe':
            recipe['name'] = d['name']
            recipe['description'] = d['description']
            recipe['ingredients'] = d['recipeIngredient']
            recipe['instructions'] = split(r'\r\n', d['recipeInstructions'])
            recipe['instructions'] = [instruction for instruction in recipe['instructions'] if instruction]
            recipe['image'] = d['image']

        return recipe

    def Parse(self, url):
        recipe = {}
        recipe['url'] = url
        recipe['source'] = 'akispetretzikis.com'

        soup = self.fetch_soup(url)

        results = soup.find_all('script', {'type': 'application/ld+json'})
        for result in results:
            d = json.loads(result.contents[0])
            if d['@type'].lower() == 'recipe':
                parsed_recipe = self.get_json_recipe(d)
                recipe.update(parsed_recipe)
            else:
                continue
        return recipe

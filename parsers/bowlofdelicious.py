import json

from parsers.recipe import Recipe

class Bowlofdelicious(Recipe):

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
            recipe['instructions'] = [i['text'] for i in r['recipeInstructions']]
            recipe['image'] = r['image'][0]

        return recipe

    def Parse(self, url):
        recipe = {}
        recipe['url'] = url
        recipe['source'] = 'bowlofdelicious.com'

        soup = self.fetch_soup(url)

        result = soup.find('script', {'type': 'application/ld+json'})

        d = json.loads(result.contents[0])
        parsed_recipe = self.get_json_recipe(d)
        recipe.update(parsed_recipe)

        return recipe

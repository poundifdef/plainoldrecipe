import json

from parsers.recipe import Recipe

class Kochbar(Recipe):

    def get_json_recipe(self, d):
        recipe = {}               

        recipe['name'] = d['name']
        recipe['description'] = d['description']
        recipe['ingredients'] = d['recipeIngredient']
        recipe['instructions'] = [i['text'] for i in d['recipeInstructions']]
        recipe['image'] = d['image']

        return recipe

    def Parse(self, url):
        recipe = {}
        recipe['url'] = url
        recipe['source'] = 'kochbar.de'

        soup = self.fetch_soup(url)
        
        result = soup.find_all('script', {'type': 'application/ld+json'})
        
        d = json.loads(result[1].contents[0])
        parsed_recipe = self.get_json_recipe(d)
        recipe.update(parsed_recipe)

        return recipe

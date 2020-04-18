from parsers.recipe import Recipe
import json

class Letsdishrecipes(Recipe):

    def get_json_recipe(self, r):
        recipe = {}
    
        recipe['name'] = r['name']
        recipe['description'] = r['description']
        recipe['ingredients'] = r['recipeIngredient']
        recipe['instructions'] = [i['text'] for i in r['recipeInstructions']]
        recipe['image'] = r['image'][0]
    
        return recipe

    def Parse(self, url):
        recipe = {}
        recipe['url'] = url
        recipe['source'] = 'letsdishrecipes.com'

        soup = self.fetch_soup(url)
        body = soup.find('body')
        result = body.find('script', {'type': 'application/ld+json'})
        d = json.loads(result.contents[0])
        parsed_recipe = self.get_json_recipe(d)
        recipe.update(parsed_recipe)

        return recipe
import json
import re
from parsers.recipe import Recipe

class EssenUndTrinken(Recipe):

    def get_json_recipe(self, d):
        recipe = {}    
        
        recipe['name'] = d['name']
        recipe['description'] = d.get('description', '')    
        recipe['ingredients'] = d['recipeIngredient']
        recipe['instructions'] = d['recipeInstructions']
        recipe['image'] = d['image'][0]['url']

        return recipe

    def Parse(self, url):
        recipe = {}
        recipe['url'] = url
        recipe['source'] = 'essen-und-trinken.de'

        soup = self.fetch_soup(url)

        result = soup.find_all('script', {'type': 'application/ld+json'})
        
        d = json.loads(result[0].contents[0])[0]
                
        parsed_recipe = self.get_json_recipe(d)
        recipe.update(parsed_recipe)

        return recipe
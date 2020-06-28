import json
import re
from parsers.recipe import Recipe

class EssenUndTrinken(Recipe):

    def get_json_recipe(self, d):
        recipe = {}    
        
        recipe['name'] = d['name']
        recipe['description'] = d['description']
        recipe['ingredients'] = d['recipeIngredient']
        recipe['instructions'] = self.cleanhtml(d['recipeInstructions']).split('\n')
        recipe['image'] = d['image']

        return recipe

    def Parse(self, url):
        recipe = {}
        recipe['url'] = url
        recipe['source'] = 'essen-und-trinken.de'

        soup = self.fetch_soup(url)

        result = soup.find_all('script', {'type': 'application/ld+json'})
        
        d = json.loads(result[1].contents[0])
                
        parsed_recipe = self.get_json_recipe(d)
        recipe.update(parsed_recipe)

        return recipe
    
    def cleanhtml(self, txt):
        cleanr = re.compile('<.*?>')        
        return re.sub(cleanr, '', txt.lstrip(" \n"))
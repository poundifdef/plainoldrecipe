import json
from parsers.recipe import Recipe


class ThatLowCarbLife(Recipe):

    def get_json_recipe(self, soup):
        recipe = {'name': soup['name'], 'description': soup['description'], 'ingredients': soup['recipeIngredient']}

        try:  # This alone works for 9/10 tested recipes
            recipe['instructions'] = [i['text'] for i in soup['recipeInstructions']]
        except TypeError:  # https://thatlowcarblife.com/big-mac-chaffle/ throws TypeError
            recipe['instructions'] = soup['recipeInstructions']
            recipe['instructions'] = list(recipe['instructions'].split("\n"))
            recipe['instructions'] = list(filter(None, recipe['instructions']))

        recipe['image'] = soup['image'][0]

        return recipe

    def Parse(self, url):
        recipe = {'url': url}

        soup = self.fetch_soup(url)
        result = soup.find_all('script', {'type': 'application/ld+json'})

        decoded_result = json.loads(result[1].contents[0])
        parsed_recipe = self.get_json_recipe(decoded_result)

        recipe.update(parsed_recipe)

        return recipe

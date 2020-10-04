import json

from parsers.recipe import Recipe

class Hervecuisine(Recipe):

    def parse_microformat(self, soup):
        recipe = {}

        name = soup.find('h1', {'class': 'post-title'})
        recipe['name'] = name.contents[0].strip()

        image = soup.find('div', {'class': 'recipe-image'})
        recipe['image'] = image.contents[0]['data-src']

        recipe['ingredients'] = []
        ingredients = soup.find_all('li', {'itemprop': 'recipeIngredient'})
        for ingredient in ingredients:
            if ingredient.find('div'):
                ingredient = ingredient.find('div')
            elif ingredient.find('span'):
                ingredient = ingredient.find('span')
            recipe['ingredients'].append(ingredient.contents[0])

        recipe['instructions'] = []
        instructions = soup.find('div', {'itemprop': 'recipeInstructions'})
        for instruction in instructions.find_all('li'):
            recipe['instructions'].append(instruction.contents[0])

        return recipe

    def Parse(self, url):
        recipe = {}
        recipe['url'] = url
        recipe['source'] = 'hervecuisine.com'

        soup = self.fetch_soup(url)

        parsed_recipe = self.parse_microformat(soup)
        recipe.update(parsed_recipe)

        return recipe

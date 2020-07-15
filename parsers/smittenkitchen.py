import json

from parsers.recipe import Recipe

class Smittenkitchen(Recipe):

    def parse_microformat(self, soup):
        recipe = {}
        #r = soup.find('div', {'class': 'h-recipe'})

        name = soup.find('h3', {'class': 'p-name'})
        recipe['name'] = name.contents[0]

        result = soup.find('meta', {'property': 'og:description'})
        recipe['description'] = result['content']

        result = soup.find('meta', {'property': 'og:image'})
        recipe['image'] = result['content']

        recipe['ingredients'] = []
        ingredients = soup.find_all('li', {'class': 'p-ingredient'})
        for ingredient in ingredients:
            recipe['ingredients'].append(ingredient.contents[0])

        recipe['instructions'] = []
        instructions = soup.find('div', {'class': 'e-instructions'})
        recipe['instructions'].append(instructions.find('p').previousSibling)

        for instruction in instructions.find_all('p'):
            recipe['instructions'].append(instruction.contents[0])

        return recipe

    def Parse(self, url):
        recipe = {}
        recipe['url'] = url
        recipe['source'] = 'smittenkitchen.com'

        soup = self.fetch_soup(url)
        parsed_recipe = self.parse_microformat(soup)
        recipe.update(parsed_recipe)

        return recipe

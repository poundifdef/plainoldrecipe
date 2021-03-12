from parsers.recipe import Recipe

class Fattoincasadabenedetta(Recipe):

    def parse_microformat(self, soup):
        recipe = {}

        title = soup.find('h1', {'class': 'entry-title'})
        recipe['name'] = title.contents[0]

        result = soup.find('meta', {'property': 'og:description'})
        recipe['description'] = result['content']

        times = soup.find('div', {'class': 'recipe-time-box'}).find_all('li')
        for time in times:
            time_element = time.find('span', {'class': 'time-text'}).contents[0]
            time_value = time.find('span', {'class': ''}).contents[0]
            recipe['description'] += "\n" + str(time_element) + ' ' + str(time_value)

        result = soup.find('meta', {'property': 'og:image'})
        recipe['image'] = result['content']

        recipe['ingredients'] = []
        ingredients = soup.find_all('li', {'class': 'wpurp-recipe-ingredient'})
        for ingredient in ingredients:
            quantity = ingredient.find('span', {'class': 'wpurp-recipe-ingredient-quantity recipe-ingredient-quantity'}).string or ''
            unit = ingredient.find('span', {'class': 'wpurp-recipe-ingredient-unit recipe-ingredient-unit'}).string or ''
            name_element = ingredient.find('span', {'class': 'wpurp-recipe-ingredient-name recipe-ingredient-name'})
            name = name_element.contents[0]
            notes = ''
            if len(name_element.contents) > 1:
                notes = name_element.contents[1].contents[0]

            recipe['ingredients'].append(quantity + ' ' + unit + ' ' + name + notes)

        recipe['instructions'] = []
        instructions = soup.find_all('li', {'class': 'wpurp-recipe-instruction'})
        for instruction in instructions:
            if instruction.contents[0].string is not None:
                recipe['instructions'].append(instruction.contents[0].string)

        return recipe

    def Parse(self, url):
        recipe = {}
        recipe['url'] = url
        recipe['source'] = 'fattoincasadabenedetta.it'

        soup = self.fetch_soup(url)
        parsed_recipe = self.parse_microformat(soup)
        recipe.update(parsed_recipe)

        print(soup.len)

        return recipe
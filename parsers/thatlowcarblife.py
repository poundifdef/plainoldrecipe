from parsers.recipe import Recipe

class ThatLowCarbLife(Recipe):

    def scrape_recipe(self, soup):
        recipe = {}

        name = soup.find('h2', {'class': 'mv-create-title'})
        recipe['name'] = name.contents[0]

        description = soup.find('div', {'class': 'mv-create-description'})
        recipe['description'] = description.contents[0].text

        image = soup.find('header', {'class': 'mv-create-header'})
        recipe['image'] = image.contents[1]['src']

        recipe['ingredients'] = []
        ingredients = soup.find('div', {'class': 'mv-create-ingredients'}).find('ul').findChildren('li')
        for li in ingredients:
            recipe['ingredients'].append(li.text)

        recipe['instructions'] = []
        instructions = soup.find('div', {'class': 'mv-create-instructions'}).find('ol').findChildren('li')
        for li in instructions:
            recipe['instructions'].append(li.text)

        return recipe


    def Parse(self, url):
        recipe = {}
        recipe['url'] = url
        recipe['source'] = 'thatlowcarblife.com'

        soup = self.fetch_soup(url)
        parsed_recipe = self.scrape_recipe(soup)
        recipe.update(parsed_recipe)

        return recipe
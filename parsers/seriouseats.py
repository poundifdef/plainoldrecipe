from parsers.recipe import Recipe

class Seriouseats(Recipe):

    def scrape_recipe(self, soup):
        recipe = {}

        name = soup.find('h1', {'class': 'title'})
        recipe['name'] = name.contents[0]

        result = soup.find('div', {'class': 'recipe-introduction-body'})
        recipe['description'] = result.contents[3].text

        try:  # try-except: https://www.seriouseats.com/recipes/2018/10/yeasted-pumpkin-bread.html breaks this due to it using a video, not <img>
            result = soup.find('div', {'class': 'se-pinit-image-container'})
            recipe['image'] = result.contents[1]['src']
        except AttributeError:
            recipe['image'] = None

        recipe['ingredients'] = []
        ingredients = soup.find_all('li', {'class': 'ingredient'})
        for ingredient in ingredients:
            recipe['ingredients'].append(ingredient.text)

        recipe['instructions'] = []
        divs = soup.find_all('div', {'class': 'recipe-procedure-text'})
        for div in divs:
            recipe['instructions'].append(div.text)

        return recipe


    def Parse(self, url):
        recipe = {}
        recipe['url'] = url
        recipe['source'] = 'seriouseats.com'

        soup = self.fetch_soup(url)
        parsed_recipe = self.scrape_recipe(soup)
        recipe.update(parsed_recipe)

        return recipe
from parsers.recipe import Recipe
import recipe_scrapers


class Seriouseats(Recipe):
    def Parse(self, url):
        recipe = {}

        # Scrape the provided website using the url passed in
        scraper = recipe_scrapers.scrape_me(url)

        # Assign the recipe's dictionary's keys and values using recipe_scraper dependency
        recipe['url'] = url
        recipe['name'] = scraper.title()
        recipe['image'] = scraper.image()
        recipe['ingredients'] = scraper.ingredients()
        recipe['instructions'] = (i[3:] for i in scraper.instructions().split("\n"))  # Each ingredient starts with a number, period, and whitespace. Remove them.

        return recipe

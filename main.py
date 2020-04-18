from flask import Flask, render_template, request, jsonify, redirect, make_response, url_for, flash
from recipe_scrapers import scrape_me, WebsiteNotImplementedError, SCRAPERS
import urllib
import parsers
import logging

app = Flask(__name__)

def scrape_recipe(url):
    recipe = {}

    try:
        scraper = scrape_me(url)
        recipe = {
            'name': scraper.title(),
            'ingredients': scraper.ingredients(),
            'instructions': scraper.instructions().split("\n"),
            'image': scraper.image(),
            'url': url,
        }
    except WebsiteNotImplementedError:
        pass

    if not recipe:
        parsed_uri = urllib.parse.urlparse(url)
        domain = parsed_uri.netloc.lower()
        parser = parsers.getParser(domain)

        if parser is None:
            return None

        recipe = parser.Parse(url)

        #try:
        #    recipe = parser.Parse(url)
        #except:
        #    return recipe

    return recipe

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recipe')
def recipe():
    url = request.args['url']
    parsed_uri = urllib.parse.urlparse(url)
    domain = parsed_uri.netloc.lower()

    try:
        recipe = scrape_recipe(url)
        if recipe is None:
            return render_template('unsupported.html', domain=domain)

        return render_template('recipe.html', recipe=recipe)
    except:
        logging.exception(url)
        return render_template('parse_error.html', domain=domain)

@app.route('/supported-websites')
def supported_websites():
    sites = list(SCRAPERS.keys())
    sites += parsers.PARSERS
    sites.sort()

    return render_template('supported.html', sites=sites)

if __name__ == '__main__':
    app.run('localhost', 8080, debug=True, threaded=True)
from flask import Flask, render_template, request, jsonify, redirect, make_response, url_for, flash
from recipe_scrapers import scrape_me, WebsiteNotImplementedError, SCRAPERS
import urllib
import parsers
import logging

app = Flask(__name__)

def scrape_recipe(url):
    recipe = {}

    parsed_uri = urllib.parse.urlparse(url)
    domain = parsed_uri.netloc.lower()
    domain = domain.replace('www.', '', 1) if domain.startswith('www.') else domain
    parser = parsers.getParser(domain)

    if parser is not None:
        recipe = parser.Parse(url)

    if not recipe:
        try:
            scraper = scrape_me(url)
            instructions = [i.strip() for i in scraper.instructions().split("\n") if i.strip()]
            recipe = {
                'name': scraper.title(),
                'ingredients': scraper.ingredients(),
                'instructions': instructions,
                'image': scraper.image(),
                'url': url,
            }
        except WebsiteNotImplementedError:
            pass

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
        if not recipe:
            return render_template('unsupported.html', domain=domain)

        return render_template('recipe.html', recipe=recipe)
    except:
        logging.exception(url)
        return render_template('parse_error.html', domain=domain)

@app.route('/supported-websites')
def supported_websites():
    sitesSet = SCRAPERS.keys()
    sitesSet |= set(parsers.PARSERS.keys())
    sites = list(sitesSet)
    sites.sort()

    return render_template('supported.html', sites=sites)

if __name__ == '__main__':
    app.run('localhost', 8080, debug=True, threaded=True)

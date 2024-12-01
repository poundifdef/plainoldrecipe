from flask import Flask, render_template, request, jsonify, redirect, make_response, url_for, flash
from recipe_scrapers import scrape_html, WebsiteNotImplementedError, SCRAPERS
import urllib
import parsers
import logging
import sys
import requests
import os

app = Flask(__name__)

def _record(website, status, recipe=''):
    if not website:
        return

    print(f"Fetched recipe: {website} {status} {recipe}", file=sys.stderr)

def _query(q):
    return []
    rc = requests.get(
        'https://demo02.scratchdb.com/query', 
        headers={'X-API-KEY': os.environ.get('SCRATCHDB_API_KEY')}, 
        params={'q': q})
    
    if rc.status_code == 200:
        return rc.json()

    print(rc.text)
    return []

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
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
            }
            resp = requests.get(url, headers=headers).text
            scraper = scrape_html(resp, org_url=url, supported_only=False)
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
            _record(domain, 'Not Supported', url)
            return render_template('unsupported.html', domain=domain), 501

        _record(domain, 'Success', url)
        return render_template('recipe.html', recipe=recipe)
    except:
        _record(domain, 'Error', url)
        logging.exception(url)
        return render_template('parse_error.html', domain=domain), 418

@app.route('/supported-websites')
def supported_websites():
    sitesSet = SCRAPERS.keys()
    sitesSet |= set(parsers.PARSERS.keys())
    sites = list(sitesSet)
    sites.sort()

    return render_template('supported.html', sites=sites)

@app.route('/statistics')
def statistics():
    not_supported = _query("select website, count(distinct recipe) as c from plainoldrecipe where status = 'Not Supported' and toYYYYMM(ULIDStringToDateTime(__row_id)) >= toYYYYMM(now()) and website != '' group by website order by c desc, website asc")
    return render_template('statistics.html', not_supported=not_supported)

if __name__ == '__main__':
    app.run('localhost', debug=True, threaded=True)

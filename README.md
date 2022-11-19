This program parses recipes from common websites and displays them using
plain-old HTML.

You can use it here: https://www.plainoldrecipe.com/

Screenshots
-----------

Home Page:
![Home Page](/screenshots/home.png?raw=true "Home Page")

View the recipe in your browser:
![Recipe](/screenshots/screen.png?raw=true "Recipe")

If you print the recipe, shows with minimal formatting:
![Print View](/screenshots/print.png?raw=true "Print View")

Building Locally
------
1. Install Python 3.6 or newer
2. `git clone https://github.com/poundifdef/plainoldrecipe.git` or download the source and extract
3. `cd plainoldrecipe`
4. [Create a virtual environment](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments) (*optional*)
5. `pip install -r requirements.txt`
6. `python app.py`

If all goes well you should see something along the lines of:
```
python main.py
 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 123-456-789
 * Running on http://localhost:8080/ (Press CTRL+C to quit)
```
After which simply navigate to the appropriate URL as displayed on the last line.

Deploy
------

`flyctl deploy`

Acknowledgements
----------------

- https://github.com/hhursev/recipe-scrapers
- https://evenbettermotherfucking.website/

Contributing
------------

1. If you want to add a new scraper, please feel free to make a PR. Your diff
   should have exactly two files: `parsers/__init__.py` and add a new class
   in the `parsers/` directory. [Here is an example](https://github.com/poundifdef/plainoldrecipe/commit/cac857c1abb1a8cb674a2a63ebb24df0c00aa666) of what your commit might
   look like.

2. If you want to fix a bug in an existing scraper, please feel free to do so,
   and include an example URL which you aim to fix. Your PR should modify exactly
   one file, which is the corresponding module in the `parsers/` directory.

3. If you want to make any other modification or refactor: please create an
   issue and ask prior to making your PR. Of course, you are welcome to fork,
   modify, and distribute this code with your changes in accordance with the LICENSE.

4. I don't guarantee that I will keep this repo up to date, or that I will respond
   in any sort of timely fashion! Your best bet for any change is to keep PRs small
   and focused on the minimum changeset to add your scraper :)

Testing PRs Locally
===================

git fetch origin pull/ID/head:BRANCHNAME

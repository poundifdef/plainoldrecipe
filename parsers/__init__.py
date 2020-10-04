from parsers.gimmesomeoven import Gimmesomeoven
from parsers.smittenkitchen import Smittenkitchen
from parsers.letsdishrecipes import Letsdishrecipes
from parsers.lovingitvegan import Lovingitvegan
from parsers.minimalistbaker import Minimalistbaker
from parsers.bowlofdelicious import Bowlofdelicious
from parsers.chefkoch import Chefkoch
from parsers.hostthetoast import Hostthetoast
from parsers.lecker import Lecker
from parsers.essenundtriken import EssenUndTrinken
from parsers.kuechengoetter import Kuechengoetter
from parsers.kochbar import Kochbar
from parsers.hostthetoast import Hostthetoast
from parsers.thewoksoflife import Thewoksoflife
from parsers.glebekitchen import GlebeKitchen
from parsers.akispetretzikis import AkisPetretzikis
from parsers.hervecuisine import Hervecuisine

# Must exclude the "www" portion of the URL
PARSERS = {
    'gimmesomeoven.com': Gimmesomeoven,
    'smittenkitchen.com': Smittenkitchen,
    'letsdishrecipes.com': Letsdishrecipes,
    'lovingitvegan.com': Lovingitvegan,
    'minimalistbaker.com': Minimalistbaker,
    'chefkoch.de': Chefkoch,
    'bowlofdelicious.com': Bowlofdelicious,
    'hostthetoast.com': Hostthetoast,
    'lecker.de': Lecker,
    'essen-und-trinken.de': EssenUndTrinken,
    'kuechengoetter.de' : Kuechengoetter,
    'kochbar.de' : Kochbar,
    'thewoksoflife.com': Thewoksoflife,
    'glebekitchen.com': GlebeKitchen,
    'akispetretzikis.com': AkisPetretzikis,
    'hervecuisine.com': Hervecuisine
}

def getParser(domain):
    parser = PARSERS.get(domain)
    if not parser:
        return None

    return parser(domain)

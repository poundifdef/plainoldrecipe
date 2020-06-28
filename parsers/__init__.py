from parsers.gimmesomeoven import Gimmesomeoven
from parsers.smittenkitchen import Smittenkitchen
from parsers.letsdishrecipes import Letsdishrecipes
from parsers.lovingitvegan import Lovingitvegan
from parsers.minimalistbaker import Minimalistbaker
from parsers.bowlofdelicious import Bowlofdelicious
from parsers.chefkoch import Chefkoch
from parsers.lecker import Lecker
from parsers.essenundtriken import EssenUndTrinken
from parsers.kuechengoetter import Kuechengoetter
from parsers.kochbar import Kochbar

PARSERS = {
    'www.gimmesomeoven.com': Gimmesomeoven,
    'smittenkitchen.com': Smittenkitchen,
    'letsdishrecipes.com': Letsdishrecipes,
    'lovingitvegan.com': Lovingitvegan,
    'minimalistbaker.com': Minimalistbaker,
    'www.bowlofdelicious.com': Bowlofdelicious,
    'www.chefkoch.de': Chefkoch,
    'www.lecker.de': Lecker,
    'www.essen-und-trinken.de': EssenUndTrinken,
    'www.kuechengoetter.de' : Kuechengoetter,
    'www.kochbar.de' : Kochbar,
}

def getParser(domain):
    parser = PARSERS.get(domain)
    if not parser:
        return None

    return parser()

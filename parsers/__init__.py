from parsers.gimmesomeoven import Gimmesomeoven
from parsers.smittenkitchen import Smittenkitchen
from parsers.letsdishrecipes import Letsdishrecipes
from parsers.lovingitvegan import Lovingitvegan
from parsers.minimalistbaker import Minimalistbaker
from parsers.bowlofdelicious import Bowlofdelicious
from parsers.chefkoch import Chefkoch
from parsers.hostthetoast import Hostthetoast
from parsers.acouplecooks import ACoupleCooks

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
    'acouplecooks.com': ACoupleCooks
}

def getParser(domain):
    parser = PARSERS.get(domain)
    if not parser:
        return None

    return parser()

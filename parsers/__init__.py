from parsers.smittenkitchen import Smittenkitchen
from parsers.letsdishrecipes import Letsdishrecipes
from parsers.minimalistbaker import Minimalistbaker
from parsers.essenundtriken import EssenUndTrinken
from parsers.kuechengoetter import Kuechengoetter
from parsers.thewoksoflife import Thewoksoflife
from parsers.glebekitchen import GlebeKitchen
from parsers.hervecuisine import Hervecuisine
from parsers.thatlowcarblife import ThatLowCarbLife
from parsers.dinneratthezoo import DinnerAtTheZoo
from parsers.pickledplum import PickledPlum
from parsers.realfoodwholelife import RealFoodWholeLife
from parsers.africanbites import Africanbites

# Must exclude the "www" portion of the URL
PARSERS = {
    'smittenkitchen.com': Smittenkitchen,
    'letsdishrecipes.com': Letsdishrecipes,
    'minimalistbaker.com': Minimalistbaker,
    'essen-und-trinken.de': EssenUndTrinken,
    'kuechengoetter.de' : Kuechengoetter,
    'thewoksoflife.com': Thewoksoflife,
    'glebekitchen.com': GlebeKitchen,
    'hervecuisine.com': Hervecuisine,
    'thatlowcarblife.com': ThatLowCarbLife,
    'dinneratthezoo.com': DinnerAtTheZoo,
    'pickledplum.com': PickledPlum,
    'realfoodwholelife.com': RealFoodWholeLife,
    'africanbites.com': Africanbites,
}

def getParser(domain):
    parser = PARSERS.get(domain)
    if not parser:
        return None

    return parser(domain)

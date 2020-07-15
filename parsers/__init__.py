from parsers.smittenkitchen import Smittenkitchen
from parsers.letsdishrecipes import Letsdishrecipes
from parsers.chefkoch import Chefkoch
from parsers.hostthetoast import Hostthetoast
from parsers.lecker import Lecker
from parsers.essenundtriken import EssenUndTrinken
from parsers.kuechengoetter import Kuechengoetter

# Must exclude the "www" portion of the URL
PARSERS = {
    "smittenkitchen.com": Smittenkitchen,
    "letsdishrecipes.com": Letsdishrecipes,
    "chefkoch.de": Chefkoch,
    "hostthetoast.com": Hostthetoast,
    "lecker.de": Lecker,
    "essen-und-trinken.de": EssenUndTrinken,
    "kuechengoetter.de": Kuechengoetter,
}


def getParser(domain):
    parser = PARSERS.get(domain)
    if not parser:
        return None

    return parser()

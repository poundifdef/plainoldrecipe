from parsers.gimmesomeoven import Gimmesomeoven
from parsers.smittenkitchen import Smittenkitchen

PARSERS = {
    'www.gimmesomeoven.com': Gimmesomeoven,
    'smittenkitchen.com': Smittenkitchen
}

def getParser(domain):
    parser = PARSERS.get(domain)
    if not parser:
        return None

    return parser()
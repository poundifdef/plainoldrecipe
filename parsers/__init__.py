from parsers.gimmesomeoven import Gimmesomeoven
from parsers.smittenkitchen import Smittenkitchen

def getParser(domain):
    parsers = {
        'www.gimmesomeoven.com': Gimmesomeoven,
        'smittenkitchen.com': Smittenkitchen
    }

    parser = parsers.get(domain)
    if not parser:
        return None

    return parser()
from parsers.gimmesomeoven import Gimmesomeoven

def getParser(domain):
    parsers = {
        'www.gimmesomeoven.com': Gimmesomeoven
    }

    parser = parsers.get(domain)
    if not parser:
        return None

    return parser()
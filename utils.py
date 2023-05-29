import re
class Utils:
    def getListDomain(self, data): 
        pattern = r"(?<!\S)[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?(?!\S)"
        domains = [item for item in data if re.match(pattern, item)]
        return domains
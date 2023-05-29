# assetfinder --subs-only example.com
import subprocess
import time
import re
class AssetFinderTool:
    def __init__(self, domain): 
        self.domain = domain

    def enumerate_subdomains(self): 
        startTime = time.time()
        command = ['assetfinder', '--subs-only', self.domain]

        print("[+] Start extracting using AssetFinder...")
        output = subprocess.check_output(command, universal_newlines=True)
        print("==> Extracted data:", output)

        print(f"[+] Script finish in: {time.time() - startTime}")
        
        result = list(set(output.strip().split('\n')))
        finalList = self.getListDomain(result)
        
        return finalList
    

    def getListDomain(self, data): 
        pattern = r"(?<!\S)[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?(?!\S)"
        domains = [item for item in data if re.match(pattern, item)]
        return domains
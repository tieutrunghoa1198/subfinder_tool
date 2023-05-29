from subfinder_tool import SubfinderTool
from findomain_tool import FindomainTool
from asetfinder_tool import AssetFinderTool
from amass_tool import AmassTool
import time
class SubDomainReconTool:
    def __init__(self): 
        self.domain = 'example.com'

    def run(self):
        startTime = time.time() 

        findomainList = FindomainTool(self.domain).enumerate_subdomains()
        amassList = AmassTool(self.domain).enumerate_subdomains()
        assetfinderList = AssetFinderTool(self.domain).enumerate_subdomains()
        subfinderList = SubfinderTool(self.domain).enumerate_subdomains()
        listDomain = amassList + assetfinderList + findomainList + subfinderList
        # listDomain = assetfinderList + findomainList + subfinderList
        uniqueList = list(set(listDomain))
        print(uniqueList)
        
        print(f"[+] Script finish in: {time.time() - startTime}")

        return uniqueList
    
    def writeToFile(self, listDomain): 
        with open("output.txt", "w") as file:
            # Iterate over each element in the list
            for item in listDomain:
                # Write the element to the file
                file.write(str(item) + "\n")

if __name__ == '__main__':
    # Example usage
    domain = 'example.com'
    tool = SubDomainReconTool()
    result = tool.run()
    tool.writeToFile(result)
    # Pass the list of unique subdomains to another tool or function
    print(result)  # or use the list as needed

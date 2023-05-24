import subprocess

class SubfinderTool:
    def __init__(self, domain):
        self.domain = domain
        self.subdomains = []

    def enumerate_subdomains(self):
        # Run Subfinder command and capture the output
        command = ['subfinder', '-d', self.domain]
        output = subprocess.check_output(command, universal_newlines=True)

        # Process the output to extract subdomains
        self.subdomains = list(set(output.strip().split('\n')))

    def get_unique_subdomains(self):
        return self.subdomains

if __name__ == '__main__':
    # Example usage
    domain = 'example.com'
    tool = SubfinderTool(domain)
    tool.enumerate_subdomains()
    subdomains = tool.get_unique_subdomains()

    # Pass the list of unique subdomains to another tool or function
    print(subdomains)  # or use the list as needed

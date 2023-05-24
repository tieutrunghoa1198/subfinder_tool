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

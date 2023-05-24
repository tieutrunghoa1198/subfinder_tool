from subfinder_tool import SubfinderTool

if __name__ == '__main__':
    # Example usage
    domain = 'example.com'
    tool = SubfinderTool(domain)
    tool.enumerate_subdomains()
    subdomains = tool.get_unique_subdomains()

    # Pass the list of unique subdomains to another tool or function
    print(subdomains)  # or use the list as needed

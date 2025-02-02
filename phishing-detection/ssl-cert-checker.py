import subprocess

def get_certificate_info(url):
    # Use crt.sh to get certificate information from the website
    command = f"crt.sh -h {url}"
    result = subprocess.run(command, capture_output=True, text=True)
    
    if result.returncode == 0:
        # Parse the output of crt.sh to extract relevant information
        info = result.stdout.split('\n')
        
        # Extract domains from the certificate information
        domains = []
        for line in info:
            domain_info = line.strip().split()
            if len(domain_info) >= 2 and domain_info[1] != 'www':
                domains.append(domain_info[1])
        
        return domains
    else:
        print(f"Failed to retrieve certificate information from {url}.")
        return []

def scan_domain(domains):
    # Check if the domains look nearly identical
    for i in range(len(domains) - 1):
        if domains[i] == domains[i + 1]:
            print(f"The domains {domains[i]} and {domains[i + 1]} are almost identical.")
    
    # If all domains are different, try to find a similar domain
    for i in range(len(domains)):
        for j in range(i + 1, len(domains)):
            if domains[i] == domains[j]:
                print(f"The domains {domains[i]} and {domains[j]} have the same domain name.")
    
    # If no similar domains are found, try to find a similar file
    for i in range(len(domains)):
        for j in range(i + 1, len(domains)):
            if domains[i] == domains[j]:
                print(f"The domains {domains[i]} and {domains[j]} have the same filename.")
    
    # If no similar domains or files are found, check if there are similar IP addresses
    for i in range(len(domains)):
        for j in range(i + 1, len(domains)):
            if domains[i] == domains[j]:
                print(f"The domains {domains[i]} and {domains[j]} have the same IP address.")
    
    # If all domains or files are similar or different, report that they belong to the same scammer
    for i in range(len(domains)):
        for j in range(i + 1, len(domains)):
            if domains[i] == domains[j]:
                print(f"The domains {domains[i]} and {domains[j]} belong to the same scammer.")

# Example usage
domains = ["example.com", "anotherdomain.com", "sameipaddress.com"]
scan_domain(domains)

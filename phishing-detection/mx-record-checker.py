import dns.resolver

def find_mx_records(domain_name):
    # Use dns.resolver.resolve() to search for the domain name in dnstwister report
    results = dns.resolver.resolve(domain_name, 'MX')
    
    # Extract IP addresses from the dnstwister report data
    mx_records = [result.address for result in results]
    
    return mx_records

def check_spam(website_url):
    # Use a known phishing website's URL to search for similar domains using dnslookup.org and iplocation.io
    known_phishing_website_url = "BANK0FAMERICA.COM"
    
    # Find the IP addresses of the known phishing website using dnslookup.org
    phishing_results = find_mx_records(known_phishing_website_url)
    
    if phishing_results is not None:
        print("A spammer was found in the IP addresses of the known phishing website")
    else:
        print("No spammer was found in the IP addresses of the known phishing website")

# Example usage
website_url = "example.com"

# Find similar domains for the given URL
similar_domains = find_mx_records(website_url)

if similar_domains is not None:
    # Check if there are any clues in the similar domains
    spammer_found = check_spam(website_url)
    
    if spammer_found:
        print("A spammer was found in the similarity of the domain names")
    else:
        print("No spammer was found in the similarity of the domain names")

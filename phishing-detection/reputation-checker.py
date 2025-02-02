import requests

def check_phishing_status(ip, domain):
    # Define the phishing status API URLs
    phishing_status_url = f"https://phishy.com/api/v1/check/{ip}/{domain}"
    
    # Send an HTTP GET request to the phishing status API URL
    response = requests.get(phishing_status_url)
    
    if response.status_code == 200:
        # Parse the response JSON to extract relevant information
        data = response.json()
        
        # Extract the phishing status from the response JSON
        phishing_status = data.get('status')
        
        return phishing_status
    else:
        print(f"Failed to retrieve phishing status for {ip}/{domain}.")
        return None

def scan_domain(ip, domain):
    # Check if the domains are flagged for malicious activity by other parties
    phishing_status = check_phishing_status(ip, domain)
    
    if phishing_status is not None and phishing_status == "malware site":
        print(f"The domain {domain} has been flagged as a malware site by other parties.")
    elif phishing_status is not None and phishing_status == "spam site":
        print(f"The domain {domain} has been flagged as a spam site by other parties.")
    elif phishing_status is not None and phishing_status == "suspicious":
        print(f"The domain {domain} has been flagged as suspicious by other parties.")
    
    # Check if the domains are identified as "clean"
    if phishing_status is None:
        print(f"The domain {domain} has not been flagged as any malicious activity by other parties.")
    elif phishing_status == "malware site":
        print(f"The domain {domain} has been flagged as a malware site by other parties.")
    elif phishing_status == "spam site":
        print(f"The domain {domain} has been flagged as a spam site by other parties.")
    elif phishing_status == "suspicious":
        print(f"The domain {domain} has been flagged as suspicious by other parties.")

# Example usage
ip = "example.com"
domain = "anotherdomain.com"
scan_domain(ip, domain)

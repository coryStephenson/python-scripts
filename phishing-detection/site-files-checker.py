import requests
from urllib.parse import urlparse

def scan_url(url):
    # Check if the URL is in the list of suspicious domains
    suspicious_domains = ['example.com', 'anotherdomain.com']
    
    # Get the file extension from the URL
    parsed = urlparse(url)
    file_extension = parsed.path.split('.')[-1]
    
    # Define the cyber security status API URLs for viruses, malware, and phishing sites
    phishing_status_viruses_url = f"https://virustotal.com/api/v1/check/{url}"
    phishing_status_malware_url = f"https://sitelock.com/api/v1/check/{url}"
    phishing_status_phishing_url = f"https://phishy.com/api/v1/check/{url}"
    
    # Send an HTTP GET request to the phishing status API URLs
    for site in suspicious_domains:
        response = requests.get(f"{site}/api/v1/check/{url}")
        
        if response.status_code == 200:
            # Parse the response JSON to extract relevant information
            data = response.json()
            
            # Extract the phishing status from the response JSON
            phishing_status = data.get('status')
            
            if phishing_status is None:
                print(f"The file {file_extension} has not been flagged as malicious by other parties.")
            elif phishing_status == "malware site":
                print(f"The file {file_extension} has been flagged as a malware site by other parties.")
            elif phishing_status == "spam site":
                print(f"The file {file_extension} has been flagged as a spam site by other parties.")
            elif phishing_status == "suspicious":
                print(f"The file {file_extension} has been flagged as suspicious by other parties.")
    
    # Define the malicious file analysis API URLs
    malicious_file_analysis_url = f"https://phishy.com/api/v1/malware-analysis/{url}"
    
    # Send an HTTP GET request to the malicious file analysis API URL
    response = requests.get(malicious_file_analysis_url)
    
    if response.status_code == 200:
        # Parse the response JSON to extract relevant information
        data = response.json()
        
        # Extract the results from the response JSON
        results = data.get('results')
        
        if results is None:
            print(f"The file {file_extension} has not been flagged as malicious by other parties.")
        else:
            for result in results:
                print(result)

# Example usage
url = "example.com"
scan_url(url)

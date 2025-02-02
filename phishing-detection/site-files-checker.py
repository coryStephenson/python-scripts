import requests
from pyvirustotal import AntiVirus

# Define the URL pattern
url_pattern = "https://scamadviser.com/scam"

def scan_file(url):
    # Use pyvirustotal to check if the file is safe
    vt = AntiVirus(api_key='your_virustotal_api_key')
    response = vt.check(url)
    
    if response['result'] == 'clean':
        print(f"The file {url} has not been flagged as malicious.")
    elif response['result'] == 'high':
        print(f"The file {url} has been flagged as potentially malicious due to its high risk of harm or infection.")
    else:
        print(f"An unknown result occurred for the file {url}.")
    
    return response

def check_website(ip, domain):
    # Send a GET request to the IP address and domain
    url = f"http://{ip}:{domain}"
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse JSON response from Virustotal
        file_info = scan_file(url)
        
        # Check if the file has been downloaded from the suspicious website in the past
        past_downloads = []
        for download in response.json()['downloads']:
            if download['url'] in ip_domain_pattern:
                past_downloads.append(download['url'])
        
        # Check if the files have been reported negatively about them
        reports = []
        for report in file_info['files']:
            for report_url in report['downloaded_urls']:
                if report_url in past_downloads:
                    reports.append(report)
        
        # If any suspicious files were found, send an unopened file to these sites
        for report in reports:
            print(f"Sending an unopened file from {report['url']} to scan.")
    
    return response

# Define the pattern for IP and domain
ip_domain_pattern = "your_ip_domain_pattern"

# Example usage
scan_website("192.168.0.1", "example.com")

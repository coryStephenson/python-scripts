import requests

def get_ip_usage(ip):
    # Define the IP usage API URLs for different sites on the same IP
    ip_usage_viruses_url = f"https://spyonweb.com/api/v1/ip/usage/{ip}"
    ip_usage_malware_url = f"https://spyonweb.com/api/v1/ip/usage/{ip}"
    
    # Send an HTTP GET request to the API URLs
    response = requests.get(ip_usage_viruses_url)
    
    if response.status_code == 200:
        # Parse the response JSON to extract relevant information
        data = response.json()
        
        # Extract the IP usage from the response JSON
        ip_usage = data.get('ip_usage')
        
        return ip_usage
    else:
        print(f"Failed to retrieve IP usage information for {ip}")
        return None

def check_spyonweb(ip):
    # Use the get_ip_usage function to get the IP usage information
    ip_usage = get_ip_usage(ip)
    
    if ip_usage is not None:
        # Define the spyonweb API URLs for different sites on the same IP
        spyonweb_viruses_url = f"https://spyonweb.com/api/v1/ip/virus/{ip}"
        spyonweb_malware_url = f"https://spyonweb.com/api/v1/ip/malware/{ip}"
    
        # Send an HTTP GET request to the API URLs
        response = requests.get(spyonweb_viruses_url)
        
        if response.status_code == 200:
            # Parse the response JSON to extract relevant information
            data = response.json()
            
            # Extract the spyonweb usage from the response JSON
            spyonweb_usage = data.get('usage')
            
            return spyonweb_usage
        else:
            print(f"Failed to retrieve spyonweb usage information for {ip}")
            return None

# Example usage
url = "example.com"
spyonweb_info = check_spyonweb(url)
if spyonweb_info is not None:
    print("IP Usage Information:")
    print(spyonweb_info)

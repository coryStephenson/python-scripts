import requests

def run_phishing_scams(url):
    # List of URLs to test against
    urls_to_test = [
        "https://scamadviser.com/scam",
        "http://urlscan.io/detect",
        "http://checkphish.ai"
    ]
    
    for url in urls_to_test:
        try:
            # Send a GET request to the URL
            response = requests.get(url)
            
            if response.status_code == 200:
                print(f"Results from {url}:")
                # Parse JSON responses
                data = response.json()
                
                if 'results' in data:
                    results = data['results']
                    for result in results:
                        if 'type' in result and 'status' in result:
                            print(f"{result['type']} URL: {result['status']}")
                        elif 'description' in result:
                            print(result['description'])
                else:
                    print(f"No information found for {url}")
            else:
                print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while accessing {url}: {e}")

# Example usage
run_phishing_scams("https://scamadviser.com/scam")

import requests

def get_tracking_ids(website_url):
    # Define the API URL for retrieving the tracking IDs of each website on the domain
    api_url = f"https://spyonweb.com/api/v1/tracking/{website_url}"
    
    # Send an HTTP GET request to the API endpoint
    response = requests.get(api_url)
    
    if response.status_code == 200:
        # Parse the JSON object containing the tracking IDs of each website on the domain
        data = response.json()
        
        return data.get('tracking_ids')
    else:
        print(f"Failed to retrieve tracking IDs for {website_url}")
        return None

def check_spam(website_url):
    # Extract the tracking IDs from the API response
    tracking_ids = get_tracking_ids(website_url)
    
    if tracking_ids is not None:
        # Check if there are any clues in the tracking IDs
        for clue in tracking_ids.values():
            if isinstance(clue, str) and "spam" in clue:
                return True
        
        return False

# Example usage
website_url = "example.com"

# Retrieve the tracking IDs of all websites on the domain
tracking_ids = get_tracking_ids(website_url)

if tracking_ids is not None:
    # Check if there are any clues in the tracking IDs
    spammer_found = check_spam(website_url)
    
    if spammer_found:
        print("A spammer was found in the tracking IDs")
    else:
        print("No spammer was found in the tracking IDs")

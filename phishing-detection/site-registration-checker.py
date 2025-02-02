import requests

def get_whois_history(whois_xml):
    # Define the API URL for retrieving historical whois history information
    api_url = "https://drs.whoisxmlapi.com/whois-history"
    
    # Send an HTTP GET request to the API endpoint
    response = requests.get(api_url, params={'WhoisXML': whois_xml})
    
    if response.status_code == 200:
        # Parse the JSON object containing the historical data
        data = response.json()
        
        return data
    else:
        print(f"Failed to retrieve historical whois history information")
        return None

def check_spammer(whois_xml):
    # Extract the contact information from the whois XML
    contact_info = whois_xml.get("ContactInfo")
    
    if contact_info is not None:
        # Check if there are any clues in the contact information
        for clue in contact_info.values():
            if isinstance(clue, str) and "spam" in clue:
                return True
        
        return False

# Example usage
whois_xml = """
<WhoisXML>
    <ContactInfo>
        <Name>John Doe</Name>
        <Email>john.doe@example.com</Email>
        <PhoneNumber>123-456-7890</PhoneNumber>
        <Address>Main Street 1, Anytown, USA 12345</Address>
    </ContactInfo>
</WhoisXML>
"""

# Retrieve the whois history for the given WHOIS XML
history = get_whois_history(whois_xml)

if history is not None:
    # Check if there are any clues in the contact information
    spammer_found = check_spammer(history)
    
    if spammer_found:
        print("A spammer was found in the whois record")
    else:
        print("No spammer was found in the whois record")

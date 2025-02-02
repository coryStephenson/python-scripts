import re

def detect_phishing(url):
    # Regular expression pattern for URLs that look suspicious
    phishing_patterns = [
        r'https://bitly\.com\/[0-9]+',
        r'https://tinyurl\.com\/[a-zA-Z0-9]{16}',
        r'https://tiny.cc\/[0-9]+',
        r'https://cutt.ly\/[a-zA-Z0-9]{16}',
        r'https://shorturl\.at\/[0-9]+'
    ]
    
    # Check each pattern in the list
    for pattern in phishing_patterns:
        if re.search(pattern, url):
            return True
    
    return False

# Example usage
url_to_check = "https://tinyurl.com/12345678"
if detect_phishing(url_to_check):
    print("The URL is suspicious and has been shortened.")
else:
    print("The URL appears to be safe or unshortened.")

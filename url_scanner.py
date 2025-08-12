# url_scanner.py
import requests
from urllib.parse import urlparse

# List of suspicious keywords often seen in phishing URLs
SUSPICIOUS_KEYWORDS = [
    "login", "verify", "update", "secure", "account", "banking",
    "confirm", "password", "signin", "credential", "billing", "payment", "security", "confirmation", "support",
  "verification", "auth", "webscr", "cmd", "protection", "claim", "appeal" 
]

def check_website_status(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return "✅ Website is online."
        else:
            return f"⚠ Website returned status code: {response.status_code}"
    except requests.RequestException:
        return "❌ Website is offline or unreachable."

def check_for_phishing(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.lower()

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in domain:
            return f"⚠ Suspicious keyword detected in domain: '{keyword}'"
    return "✅ No suspicious keywords found."

if __name__ == "__main__":
    website = input("Enter the website URL (include http:// or https://): ").strip()

    print("\n[+] Checking website status...")
    print(check_website_status(website))

    print("\n[+] Scanning for phishing indicators...")
    print(check_for_phishing(website))

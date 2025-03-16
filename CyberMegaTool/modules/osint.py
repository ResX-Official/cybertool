import requests
import re

def gather_info(domain):
    print(f"🌍 Gathering OSINT data on {domain}...")

    # Scrape emails from the website
    try:
        response = requests.get(f"http://{domain}")
        emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", response.text))
        if emails:
            print(f"📧 Found emails: {emails}")
    except requests.exceptions.RequestException:
        print("⚠️ Error fetching domain data.")

    # Check if domain has leaked passwords
    hibp_api = f"https://haveibeenpwned.com/api/v3/breachedaccount/{domain}"
    try:
        breached = requests.get(hibp_api, timeout=5)
        if breached.status_code == 200:
            print(f"🚨 {domain} found in leaked password databases!")
        else:
            print("✅ No breaches found.")
    except requests.exceptions.RequestException:
        print("⚠️ Could not check HaveIBeenPwned API.")

    print("✅ OSINT gathering complete!")

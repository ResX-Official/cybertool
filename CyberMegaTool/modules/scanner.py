import requests
import re

def scan_target(url):
    print(f"🔍 Scanning {url} for vulnerabilities...")

    # Common payloads for SQLi and XSS
    payloads = ["'", '"', "<script>alert('XSS')</script>", "OR 1=1 --", "'; DROP TABLE users; --"]
    
    for payload in payloads:
        target_url = f"{url}?test={payload}"
        try:
            response = requests.get(target_url, timeout=5)
            if response.status_code == 200:
                if "syntax error" in response.text.lower() or "mysql" in response.text.lower():
                    print(f"🚨 Potential SQL Injection found with payload: {payload}")
                if "<script>alert('XSS')</script>" in response.text:
                    print(f"🚨 Potential XSS vulnerability detected!")
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Error connecting to {url}: {e}")

    print("✅ Scan complete!")


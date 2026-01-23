# | **Beginner** | **Web** | **12. Website Connectivity Checker** | `requests` module, handling HTTP status codes. |
import requests

url = input("Enter the URL for connectivity checking : ").strip()

if not url.startswith('http'):
    url = 'https://' + url
try:
    # Use a timeout so your program doesn't hang forever
    response = requests.get(url, timeout=5)

    code = response.status_code # is an integer
    if 200 <= code < 300 :
        print(f"✅ Success! {url} is UP. (Status: {code})")
    elif 300 <= code < 400:
        print(f"↪️ Redirect! {url} has moved. (Status: {code})")
    elif 400 <= code < 500:
        print(f"❌ Client Error! Check the URL. (Status: {code})")
    elif 500 <= code < 600:
        print(f"🔥 Server Error! It's not you, it's them. (Status: {code})")
except requests.exceptions.ConnectionError:
    print("🌐 Error: Failed to connect. Check your internet or the URL spelling.")
except requests.exceptions.Timeout:
    print("⏳ Error: The request timed out (the server took too long to respond).")
except requests.exceptions.RequestException as e:
    print(f"❓ An unexpected error occurred: {e}")
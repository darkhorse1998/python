from threading import Thread
import requests


websites = [
    "https://www.google.com",
    "https://www.github.com"
]

def getWebsite(website: str) -> None:
    try:
        response = requests.get(website)
        print(f"Response code from website {website}: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error accessing website {website}: {e}")


threads = [Thread(target=getWebsite, args=(website,)) for website in websites]
[thread.start() for thread in threads]
# [thread.join() for thread in threads]
import requests

def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
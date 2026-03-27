import urllib.request
import json

def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    print("Fetching: ", url)

    try:
        req = urllib.request.Request(url)
        req.add_header("User-Agent", "Python-CLI")

        response = urllib.request.urlopen(req)
        print("Response status: ", response.status)
        data = response.read()
        text = data.decode("utf-8")
        events = json.loads(text)
        return events
    
    except Exception as e:
        print("Error: ", e)
        return None
    
def fetch_github_url(url):
    try:
        req = urllib.request.Request(url)
        req.add_header("User-Agent", "Python-CLI")

        response = urllib.request.urlopen(req)
        print("Response Status: ", response.status)
        data = response.read()
        text = data.decode("utf-8")
        events = json.loads(text)
        return events
    except Exception as e:
        print("Error for url", e)
        return None
    
def display_events(events):
    if not events:
        print("No activity found")
        return
    print("\nRecent github activity: \n")

    for event in events[:5]:
        event_type = event["type"]
        repo_name = event["repo"]["name"]

        print(f"{event_type} in {repo_name}")

def main():

    while True:
        print("\nCLI based Github user activity\n")
        print("1. Fetch using username")
        print("2. Fetch using URL")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter the username: ")
            events = fetch_github_activity(username)
            display_events(events)
        elif choice == "2":
            print("Enter url in this format - https://api.github.com/users/{username}/events")
            url = input("Paste the url: ")
            events = fetch_github_url(url)
            display_events(events)
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
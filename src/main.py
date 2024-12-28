import argparse
from src.api import fetch_github_activity
from src.utils import format_activity

def main():
    parser = argparse.ArgumentParser(description="Fetch GitHub user recent activity")
    parser.add_argument("username", help="Github username")
    args = parser.parse_args()

    activity = fetch_github_activity(args.username)
    formatted_activity = format_activity(activity) 
    for event in formatted_activity:
        print(event)

if __name__ == "__main__":
    main()
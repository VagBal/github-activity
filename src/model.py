from dataclasses import dataclass

@dataclass
class GitHubEvent:
    event_type: str
    repo: str
    action: str

    def __str__(self):
        return f"{self.action} {self.repo}"

def parse_github_event(event):
    event_type = event['type']
    repo_name = event['repo']['name']
    action = determine_action(event)
    return GitHubEvent(event_type, repo_name, action)

def determine_action(event):
    if event['type'] == 'PushEvent':
        return f"Pushed {len(event['payload']['commits'])} commits to"
    elif event['type'] == 'IssuesEvent' and event['payload']['action'] == 'opened':
        return "Opened a new issue in"
    elif event['type'] == 'WatchEvent' and event['payload']['action'] == 'started':
        return "Started"
    else:
        return "Performed an action in"
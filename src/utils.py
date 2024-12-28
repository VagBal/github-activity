from src.model import parse_github_event

def format_activity(events):
    return [parse_github_event(event) for event in events]

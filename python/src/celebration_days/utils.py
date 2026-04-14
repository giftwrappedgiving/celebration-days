def parse_date(date_str):
    from datetime import datetime
    from dateutil import parser

    # Attempt to parse the date string
    try:
        return parser.parse(date_str)
    except ValueError:
        return None

def format_output(data):
    import json
    return json.dumps(data, indent=4)

def get_next_celebration(celebrations):
    from datetime import datetime

    today = datetime.now()
    upcoming = [c for c in celebrations if c['event_date'] > today]
    upcoming.sort(key=lambda x: x['event_date'])

    return upcoming[0] if upcoming else None
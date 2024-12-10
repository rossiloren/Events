import requests

def search_eventbrite_events(location, start_date, end_date, api_token):
    url = "https://www.eventbriteapi.com/v3/events/search/"
    params = {
        "location.address": location,
        "start_date.range_start": start_date,
        "start_date.range_end": end_date,
        "token": api_token
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()["events"]
    else:
        print(f"Errore: {response.status_code}")
        return []

# Utilizzo
if __name__ == "__main__":
    API_TOKEN = "la_tua_api_token_eventbrite"
    location = "Ancona"
    start_date = "2024-11-01T00:00:00Z"
    end_date = "2024-11-30T23:59:59Z"

    events = search_eventbrite_events(location, start_date, end_date, API_TOKEN)
    for event in events:
        print(event["name"]["text"], event["url"])


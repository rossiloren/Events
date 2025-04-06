'''
It defines how the events are structured and searched
'''


import requests
from bs4 import BeautifulSoup
from typing import Optional

from config import ConfigEvents

class Events:
    def __init__(
        self,
        area: str,
        start_date: str,
        end_date: str,
        config: ConfigEvents
    ):
        """
        Initialize the Events class.

        Parameters:
        - area: str, geographic area to search for events.
        - start_date: str, start date in YYYY-MM-DD format.
        - end_date: str, end date in YYYY-MM-DD format.
        - config: ConfigEvents, configuration object with API keys and settings.
        """
        self.area = area
        self.start_date = start_date
        self.end_date = end_date
        self.config = config

    def fetch_data(self, url: str, params: Optional[dict[str, str]] = None) -> Optional[dict]:
        """
        Performs an HTTP GET request and return the JSON response.
        Retrieves data from a specified url
            When you type https://api.example.com/events?city=Ancona in your browser
            you're making a GET request to an API, asking for event data related to Ancona.

        Parameters:
        - url: str, the URL to send the GET request to.
        - params: dict, the parameters to send with the GET request.

        Returns:
        - dict: The JSON response or None if an error occurred.
        """
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def search_google(self) -> list[dict[str, str]]:
        """Search for events on Google using the Custom Search JSON API."""
        print("Searching on Google...")
        if not self.config.google_api_key or not self.config.search_engine_id:
            print("Google API credentials are missing.")
            return []

        query = f"events in {self.area} between {self.start_date} and {self.end_date}"
        base_url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "key": self.config.google_api_key,
            "cx": self.config.search_engine_id,
            "q": query
        }

        data = self.fetch_data(base_url, params)
        return [
            {'title': item.get('title'), 'link': item.get('link'), 'snippet': item.get('snippet', '')}
            for item in data.get('items', [])
        ] if data else []

    def search_predefined_websites(self) -> list[dict[str, str]]:
        """Search for events on predefined websites."""
        print("Searching on predefined websites...")
        results = []
        for website in self.config.predefined_websites:
            response = requests.get(website)
            soup = BeautifulSoup(response.text, 'html.parser')
            for event in soup.find_all('div', class_='event'):  # Example class
                results.append({
                    'website': website,
                    'event_name': event.text,
                    'event_link': event.find('a')['href']
                })
        return results
    

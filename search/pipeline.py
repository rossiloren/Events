"""
Defines the procedures to search for events using different methods.
"""

import json

from events import Events
from config import ConfigEvents


def run_pipeline(
    area: str,
    start_date: str,
    end_date: str,
    output_path: str,
    config: ConfigEvents
) -> None:
    """
    The main pipeline for searching events using different methods.

    Parameters:
    - area: str, the area to search for events.
    - start_date: str, the start date for event search.
    - end_date: str, the end date for event search.
    - output_path: str, the file path to save results.
    - config: ConfigEvents instance with API keys and settings.
    """
    event_search = Events(area, start_date, end_date, config)
    
    # Perform searches
    results = {
        "Google Results": event_search.search_google(),
        "Predefined Websites Results": event_search.search_predefined_websites(),
    }

    # Save results to a JSON file
    with open(output_path, "w") as f:
        json.dump(results, f, indent=4)

    print(f"Results saved to {output_path}")
"""
Configuration settings for event search.
"""

from typing import Optional


class ConfigEvents:
    def __init__(
        self,
        google_api_key: str = "AIzaSyC4zKyBA9DYzSdC3ZqGvj_w350KJwRLHDI",
        search_engine_id: str = "95793f8c6ed12480a",
        predefined_websites: Optional[list[str]] = None
    ):
        """
        Initialize configuration for event searching.
        """
        self.google_api_key = google_api_key
        self.search_engine_id = search_engine_id
        self.predefined_websites = predefined_websites or ["https://example1.com", "https://example2.com"]

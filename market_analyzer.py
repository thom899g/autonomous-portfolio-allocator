import pandas as pd
from news_api_connector import NewsAPIConnector

class MarketAnalyzer:
    def __init__(self):
        self.news_connector = NewsAPIConnector()
        self.trend_detector = TrendDetector()

    def start(self):
        self.active = True
        self._fetch_data()

    def stop(self):
        self.active = False

    def _fetch_data(self):
        while self.active:
            # Fetch market data and news sentiment
            data = self.news_connector.get_sentiment()
            if data is not None:
                self.trend_detector.update(data)
            # Sleep for a short period to avoid overwhelming the API

    def analyze_trends(self, time_frame='1D'):
        return self.trend_detector.detect(time_frame)

    def get_recommendation(self):
        return self.trend_detector.recommend_strategy()
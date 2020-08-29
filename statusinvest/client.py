from typing import List

import requests
from bs4 import BeautifulSoup

from statusinvest.domain.split_grouping import SplitGrouping
from statusinvest.enums import StockTypeEnum
from statusinvest.extractors.earnings_extractor import EarningsExtractor
from statusinvest.extractors.events_extractor import EventsExtractor


class Client:
    """
    Client for statusinvest crawler. This client allows you to fetch several kind of information from their website.
    """

    def __init__(self, stock_type: StockTypeEnum, ticker: str):
        self.ticker = ticker
        self.stock_type = stock_type
        self.base_url = "https://statusinvest.com.br"
        self.bs_node = self.__initialize_beautifulsoup()

    def __build_status_invest_url(self):
        return f"{self.base_url}/{self.stock_type}/{self.ticker}"

    def __initialize_beautifulsoup(self):
        html_content = requests.get(self.__build_status_invest_url()).text
        return BeautifulSoup(html_content, "lxml")

    def get_events(self) -> List[SplitGrouping]:
        """
        :return: List of SplitGrouping objects containing all events of split and grouping for given ticker
        """
        return EventsExtractor(self.bs_node).extract_events()

    def get_earnings(self):
        """
        :return: List of Dividends objects containing all dividends for the given ticker
        """
        return EarningsExtractor().get_earnings(self.ticker)

    def get_bonuses(self):
        """
        :return: List of bonuses objects containing all bonuses for the given ticker
        """
        raise NotImplementedError

    def get_subscriptions(self):
        """
        :return: List of subscriptions every registered for the given ticker
        """
        raise NotImplementedError

import re
from datetime import datetime
from typing import List

from bs4 import BeautifulSoup

from statusinvest.domain.subscription import Subscription


class SubscriptionsExtractor:
    """
    This class is responsible for extracting subscription events from status invest
    website.
    """

    def __init__(self, parser: BeautifulSoup):
        self.parser = parser
        self.header_reference = "SUBSCRIÇÃO"
        self.events = []

    def extract_subscriptions(self) -> List[Subscription]:
        """
        :return: List of subscriptions extracted from status invest
        """
        split_grouping_rows = self.__find_subscription_rows()
        for row in split_grouping_rows:
            subscription = Subscription()
            subscription.base_value = self.__get_base_value_from_row(row)
            subscription.announcement_date = self.__get_announcement_date_from_row(row)
            subscription.reference_date = self.__get_reference_from_row(row)
            subscription.percentage = self.__get_percentage_value_from_row(row)
            subscription.received_ticker = self.__get_received_ticker_from_row(row)
            self.events.append(subscription)
        return self.events

    def __find_subscription_rows(self) -> List:
        subscriptions = self.parser.find_all(
            "small", text=re.compile("valor base", re.IGNORECASE)
        )
        return [subscription.parent.parent for subscription in subscriptions]

    @classmethod
    def __get_reference_from_row(cls, row) -> datetime.date:
        reference_date = (
            row.find("small", text=re.compile("data com", re.IGNORECASE))
            .findNext("strong")
            .text
        )
        return datetime.strptime(reference_date, "%d/%m/%Y").date()

    @classmethod
    def __get_base_value_from_row(cls, row) -> datetime.date:
        base_value = (
            row.find("small", text=re.compile("valor base", re.IGNORECASE))
            .findNext("strong")
            .text
        )
        base_value = base_value.replace("R$", "").replace(",", ".").strip()
        return float(base_value)

    @classmethod
    def __get_percentage_value_from_row(cls, row) -> datetime.date:
        percentage_value = (
            row.find("small", text=re.compile("percentual", re.IGNORECASE))
            .findNext("strong")
            .text
        )
        percentage_value = percentage_value.replace("%", "").replace(",", ".").strip()
        return float(percentage_value) / 100

    @classmethod
    def __get_received_ticker_from_row(cls, row) -> datetime.date:
        return (
            row.find("small", text=re.compile("ativo emitido", re.IGNORECASE))
            .findNext("span")
            .text
        )

    @classmethod
    def __get_announcement_date_from_row(cls, row) -> datetime.date:
        announcement_date = (
            row.find("small", text=re.compile("anúncio", re.IGNORECASE))
            .findNext("strong")
            .text
        )
        return datetime.strptime(announcement_date, "%d/%m/%Y").date()

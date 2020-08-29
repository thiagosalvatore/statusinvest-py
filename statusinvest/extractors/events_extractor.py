import re
from datetime import datetime
from typing import List, Tuple

from bs4 import BeautifulSoup

from statusinvest.domain.split_grouping import SplitGrouping
from statusinvest.enums import EventType


class EventsExtractor:
    """
    This class is responsible for extracting events of Spliting and Grouping from status invest
    website.
    """

    def __init__(self, parser: BeautifulSoup):
        self.parser = parser
        self.header_reference = "DESDOBRAMENTO/GRUPAMENTO"
        self.events = []

    def extract_events(self) -> List[SplitGrouping]:
        """
        :return: List of grouping and splits (SplitGrouping) extracted from status invest
        """
        split_grouping_rows = self.__find_splits_grouping_rows()
        for row in split_grouping_rows:
            split_grouping = SplitGrouping()
            split_grouping.event_type = self.__get_event_type_from_row(row)
            split_grouping.proportion = self.__get_factor_from_row(row)
            split_grouping.start_date = self.__get_start_date_from_row(row)
            split_grouping.announcement_date = self.__get_announcement_date_from_row(
                row
            )
            self.events.append(split_grouping)
        return self.events

    def __find_splits_grouping_rows(self) -> List:
        splits = self.parser.find_all(
            "span", text=re.compile("Desdobramento$|Grupamento$", re.IGNORECASE)
        )
        return [split.parent.parent.parent for split in splits]

    @classmethod
    def __get_event_type_from_row(cls, row) -> EventType:
        return row.find(
            "span", text=re.compile("Desdobramento$|Grupamento$", re.IGNORECASE)
        ).text.lower()

    @classmethod
    def __get_factor_from_row(cls, row) -> Tuple[float, float]:
        factor = (
            row.find("small", text=re.compile("fator", re.IGNORECASE))
            .findNext("strong")
            .text
        )
        factor_array = factor.replace(",", ".").split("para")
        start_with, end_with = float(factor_array[0]), float(factor_array[1])
        return start_with, end_with

    @classmethod
    def __get_start_date_from_row(cls, row) -> datetime.date:
        start_date = (
            row.find("small", text=re.compile("data com", re.IGNORECASE))
            .findNext("strong")
            .text
        )
        return datetime.strptime(start_date, "%d/%m/%Y").date()

    @classmethod
    def __get_announcement_date_from_row(cls, row) -> datetime.date:
        start_date = (
            row.find("small", text=re.compile("data do anúncio", re.IGNORECASE))
            .findNext("strong")
            .text
        )
        return datetime.strptime(start_date, "%d/%m/%Y").date()

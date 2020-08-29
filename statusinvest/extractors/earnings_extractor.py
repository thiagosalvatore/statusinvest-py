from datetime import datetime
from typing import List

import requests

from statusinvest.domain.earning import Earning
from statusinvest.enums import EarningType
from statusinvest.extractors.exceptions import InvalidEarningTypeException


class EarningsExtractor:
    """
    This class is responsible for extracting earnings from status invest
    website.
    """

    def get_earnings(self, ticker: str) -> List[Earning]:
        """
        Get earnings information from statusinvest API
        :param ticker: Negotiation code
        :return: List of earnings for the given ticker
        """
        earnings = requests.get(
            f'https://statusinvest.com.br/acao/companytickerprovents?ticker={ticker}&chartProventsType=2'
        )
        earnings_result = earnings.json()['assetEarningsModels']
        return [
            Earning(
                earning_type=self.__get_earning_type_from_status_invest(result['et']),
                reference_date=datetime.strptime(result['ed'], '%d/%m/%Y').date()
                if result['ed'] != '-'
                else None,
                payment_date=datetime.strptime(result['pd'], '%d/%m/%Y').date()
                if result['pd'] != '-'
                else None,
                value=result['v'],
                description=result['etd'],
            )
            for result in earnings_result
        ]

    @staticmethod
    def __get_earning_type_from_status_invest(earning_type: str):
        earning_type = earning_type.lower().strip()
        if earning_type == EarningType.DIVIDENDO.value.lower():
            return EarningType.DIVIDENDO.value
        if earning_type == EarningType.JUROS_CAPITAL_PROPRIO.value:
            return EarningType.JUROS_CAPITAL_PROPRIO.value
        if earning_type == EarningType.RENDIMENTO.value:
            return EarningType.RENDIMENTO.value
        raise InvalidEarningTypeException

from enum import Enum


class StockTypeEnum(Enum):
    """
    Types of stocks that statusinvest accepts on their urls
    """

    STOCK = 'acoes'
    ETF = 'etfs'
    FII = 'fundos-imobiliarios'


class EventType(Enum):
    """
    Types of events on statusinvest
    """

    SPLIT = 'desdobramento'
    GROUPING = 'grupamento'

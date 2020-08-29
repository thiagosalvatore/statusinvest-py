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


class EarningType(Enum):
    """
    Types of earning on statusinvest
    """

    DIVIDENDO = "dividendo"
    JUROS_CAPITAL_PROPRIO = "jcp"
    RENDIMENTO = "rendimento"

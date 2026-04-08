from collections import namedtuple


class SplitNumAndTextParams:
    """
    Класс, содержащий наборы тестовых данных для проверки
    корректной работы функции ```split_num_and_text```.
    """

    default_price = "1000000"
    default_currency = "rub"

    parametrizer = namedtuple(
        'parametrizer',
        [
            'test_title',
            'test_desc',
            'text',
            'expected_result',
        ],
    )

    formattings = [
        parametrizer(
            "Разделение пустого текста",
            "пустая строка",
            "",
            (None, None),
        ),
        parametrizer(
            "Разделение текста без пробела между ценой и валютой",
            "без пробелов между ценой и валютой",
            f"{default_price}{default_currency}",
            (default_price, default_currency),
        ),
        parametrizer(
            "Разделение текста с несколькими пробелами между ценой и валютой",
            "с несколькими пробелмами между ценой и валютой",
            f"{default_price}         {default_currency}",
            (default_price, default_currency),
        ),
        parametrizer(
            "Разделение текста со спецсимволами перед ценой",
            "со спецсимволами перед ценой",
            f"!#*^@{default_price} {default_currency}",
            (default_price, default_currency),
        ),
        parametrizer(
            "Разделение текста со спецсимволами вместо пробела",
            "со спецсимволами вместо пробела",
            f"{default_price}!#*^@{default_currency}",
            (default_price, default_currency),
        ),
        parametrizer(
            "Разделение текста со спецсимволами в валюте",
            "со спецсимволами в валюте",
            f"{default_price} !ru*bls",
            (None, None),
        ),
        parametrizer(
            "Разделение текста без указания цены",
            "без указания цены",
            f"{default_currency}",
            (None, None),
        ),
        parametrizer(
            "Разделение текста без указания валюты",
            "без указания валюты",
            f"{default_price}",
            (None, None),
        ),
    ]

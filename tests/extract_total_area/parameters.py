from collections import namedtuple


class ExtractTotalAreaParams:
    """
    Класс, содержащий наборы тестовых данных для проверки
    корректной работы функции ```extract_total_area```.
    """

    default_square_value = 1234.567

    parametrizer = namedtuple(
        'parametrizer',
        [
            'test_title',
            'test_desc',
            'text',
            'expected_result',
        ],
    )

    units_checks = [
        parametrizer(
            "Конвертация площади с единицей измерения м2",
            "с единицей измерения м2",
            f"{default_square_value} м2",
            default_square_value,
        ),
        parametrizer(
            "Конвертация площади с единицей измерения м²",
            "с единицей измерения м²",
            f"{default_square_value} м²",
            default_square_value,
        ),
        parametrizer(
            "Конвертация площади с единицей измерения кв.м",
            "с единицей измерения кв.м",
            f"{default_square_value} кв.м",
            default_square_value,
        ),
        parametrizer(
            "Конвертация площади с единицей измерения кв. м",
            "с единицей измерения кв. м",
            f"{default_square_value} кв. м",
            None,
        ),
        parametrizer(
            "Конвертация площади с единицей измерения м.кв",
            "с единицей измерения м.кв",
            f"{default_square_value} м.кв",
            default_square_value,
        ),
        parametrizer(
            "Конвертация площади с единицей измерения м. кв",
            "с единицей измерения м. кв",
            f"{default_square_value} м. кв",
            None,
        ),
        parametrizer(
            "Конвертация площади с единицей измерения М2",
            "с единицей измерения М2",
            f"{default_square_value} М2",
            None,
        ),
        parametrizer(
            "Конвертация площади с единицей измерения М²",
            "с единицей измерения М²",
            f"{default_square_value} М²",
            None,
        ),
        parametrizer(
            "Конвертация площади с единицей измерения га (гектары)",
            "с единицей измерения га (гектары)",
            f"{default_square_value} га",
            default_square_value * 100,
        ),
        parametrizer(
            "Конвертация площади с единицей измерения сот (сотки)",
            "с единицей измерения сот",
            "1234.567 сот",
            None,
        ),
        parametrizer(
            ("Конвертация площади с единицей измерения сот. (сотки) - "
             "с точкой на конце"),
            "с единицей измерения сот. (сотки) - с точкой на конце",
            f"{default_square_value} сот.",
            default_square_value,
        ),
        parametrizer(
            "Конвертация площади с единицей измерения м3",
            "с единицей измерения м3",
            f"{default_square_value} м3",
            None,
        ),
        parametrizer(
            "Конвертация площади с единицей измерения кв.миль",
            "с единицей измерения кв.миль",
            f"{default_square_value} кв.миль",
            None,
        ),
    ]

    formattings = [
        parametrizer(
            "Конвертация пустого текста",
            "",
            "",
            None,
        ),
        parametrizer(
            ("Конвертация текста без пробела между "
             "значением площади и единицей измерения"),
            "без пробела между значением площади и единицей измерения",
            f"{default_square_value}м2",
            default_square_value,
        ),
        parametrizer(
            ("Конвертация текста с несколькими пробелами между "
             "значением площади и единицей измерения"),
            ("с несколькими пробелами между значением "
             "площади и единицей измерения"),
            f"{default_square_value}       м2",
            default_square_value,
        ),
        parametrizer(
            "Конвертация текста только со значением площади",
            "только со значением площади",
            "  10   ",
            None,
        ),
        parametrizer(
            "Конвертация текста только с единицей измерения",
            "только с единицей измерения",
            "   м2",
            None,
        ),
        parametrizer(
            "Конвертация текста со спецсимволами перед значением площади",
            "со спецсимволами перед значением площади",
            f"_*&^{default_square_value}кв.м.",
            default_square_value,
        ),
        parametrizer(
            "Конвертация текста со спецсимволами вместо пробела",
            "со спецсимволами вместо пробела",
            f"{default_square_value}*?#! м2",
            None,
        ),
        parametrizer(
            "Конвертация текста с несколькими указанными единицами измерения",
            "с несколькими указанными единицами измерения",
            f"{default_square_value} кв.м. м2",
            default_square_value,
        ),
    ]

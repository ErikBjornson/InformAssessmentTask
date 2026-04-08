import allure
import pytest

from src import split_num_and_text


@allure.epic("Выполнение тестового задания")
@allure.feature("Функция возврата цены и валюты объекта из текста")
@allure.story("Тестирование конвертируемых значений цен")
class TestSplitNumAndTextCheckingPrices:
    """
    Класс с автотестами для проверки корректности возвращаемых
    значений функции ```split_num_and_text```.
    """

    @allure.title("Отделение ценового диапазона от валюты")
    @allure.description("Тест проверяет корректность отделения "
                        "ценового диапазона (например, 'от X rub') от валюты.")
    def test_try_convert_range_price(self):
        """
        Проверка корректности отделения ценового
        диапазона (например, 'от X rub') от валюты.
        """
        text = "от 100000 rub"
        expected_result = ("100000", "rub")

        current_result = split_num_and_text(text)
        assert current_result == expected_result

    @allure.title("Отделение целочисленной значения цены от валюты")
    @allure.description("Тест проверяет корректность отделения "
                        "целочисленного значения цены от валюты.")
    def test_try_convert_integer_price(self):
        """
        Проверка корректности отделения
        целочисленного значения цены от валюты.
        """
        text = "1234000 dollars"
        expected_result = ("1234000", "dollars")

        current_result = split_num_and_text(text)
        assert current_result == expected_result

    @pytest.mark.parametrize(
        'arguments',
        [
            {
                "title": ("Отделение дробного значения цены, указанного "
                          "через точку, от валюты"),
                "desc": "через точку",
                "text": "1234.56 euro",
                "result": ("1234.56", "euro"),
            },
            {
                "title": ("Отделение дробного значения цены, указанного "
                          "через запятую, от валюты"),
                "desc": "через запятую",
                "text": "1234,56 euro",
                "result": ("1234,56", "euro"),
            },
        ],
        ids=("with_point", "with_comma"),
    )
    def test_try_convert_float_price(self, arguments):
        description = """
            Тест проверяет корректность отделения дробного
            значения цены объекта, указанного {}, от валюты.
            """
        allure.dynamic.title(arguments["title"])
        allure.dynamic.description(description.format(arguments["desc"]))

        text = arguments["text"]
        expected_result = arguments["result"]

        current_result = split_num_and_text(text)
        assert current_result == expected_result

    @allure.title("Отделение нулевого значения цены от валюты")
    @allure.description("Тест проверяет корректность отделения "
                        "нулевого значения цены от валюты.")
    def test_try_convert_zero_price(self):
        """
        Проверка корректности отделения нулевого
        значения цены от валюты.
        """
        text = "0 tenge"
        expected_result = ("0", "tenge")

        current_result = split_num_and_text(text)
        assert current_result == expected_result

    @allure.title("Отделение отрицательного значения цены от валюты")
    @allure.description("Тест проверяет корректность отделения "
                        "отрицательного значения цены от валюты.")
    def test_try_convert_negative_price(self):
        """
        Проверка корректности отделения отрицательного
        значения цены от валюты.
        """
        text = "-100000 yuan"
        expected_result = (None, None)

        current_result = split_num_and_text(text)
        assert current_result == expected_result

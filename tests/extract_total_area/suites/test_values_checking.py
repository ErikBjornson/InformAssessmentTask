import allure
import pytest

from src import extract_total_area


@allure.epic("Выполнение тестового задания")
@allure.feature("Функция возврата площади объекта из текста")
@allure.story("Тестирование значений площадей")
class TestExtractTotalAreaCheckingValues:
    """
    Класс с автотестами для проверки корректности возвращаемых
    значений функции ```extract_total_area```.
    """

    @allure.title("Конвертация целочисленного значения площади")
    @allure.description("Тест проверяет, что текст, в котором площадь "
                        "указана целым числом, корректно конвертируется "
                        "в дробное число.")
    def test_try_convert_integer_square(self):
        """
        Проверка конвертации текста с указанным
        целочисленным значением площади объекта.
        """
        value = 123

        text = f"{value} м2"
        expected_result = float(value)

        current_result = extract_total_area(text)
        assert current_result == expected_result

    @pytest.mark.parametrize(
        'arguments',
        [
            {
                "title": ("Конвертация дробного значения площади, "
                          "указанного через точку"),
                "desc": "через точку",
                "square": "100.567 м2",
                "result": 100.567,
            },
            {
                "title": ("Конвертация дробного значения площади, "
                          "указанного через запятую"),
                "desc": "через запятую",
                "square": "500,234 м2",
                "result": 500.234,
            },
        ],
        ids=("with_point", "with_comma"),
    )
    def test_try_convert_float_square(self, arguments):
        description = """
            Тест проверяет, что текст, в котором площадь указана дробным
            числом {}, корректно конвертируется в дробное число.
        """
        allure.dynamic.title(arguments["title"])
        allure.dynamic.description(description.format(arguments["desc"]))

        text = arguments['square']
        expected_result = arguments['result']

        current_result = extract_total_area(text)
        assert current_result == expected_result

    @allure.title("Конвертация нулевого значения площади")
    @allure.description("Тест проверяет, что текст, в котором указано нулевое "
                        "значение площади, конвертируется как нулевое "
                        "значение площади объекта.")
    def test_try_convert_zero_square(self):
        """
        Проверка конвертации текста с указанным
        нулевым значением площади объекта.
        """
        text = "0 м2"
        expected_result = 0.0

        current_result = extract_total_area(text)
        assert current_result == expected_result

    @allure.title("Конвертация отрицательного значения площади")
    @allure.description("Тест проверяет, что текст, в котором указано "
                        "отрицательное значение площади, корректно "
                        "конвертируется как положительное дробное значение "
                        "площади объекта.")
    def test_try_convert_negative_square(self):
        """
        Проверка конвертации текста с указанным
        отрицательным значением площади объекта.
        """
        value = -123

        text = f"{value} м2"
        expected_result = abs(float(value))

        current_result = extract_total_area(text)
        assert current_result == expected_result

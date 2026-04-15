import allure
import pytest

from src import extract_total_area
from tests.extract_total_area.parameters import ExtractTotalAreaParams


@allure.epic("Выполнение тестового задания")
@allure.feature("Функция возврата площади объекта из текста")
@allure.story("Тестирование форматов вводимых площадей")
@pytest.mark.extract_total_area
class TestExtractTotalAreaCheckingFormatting:
    """
    Класс с автотестами для проверки конвертации передаваемого
    в функцию ```extract_total_area``` текста некорректного формата.
    """

    @pytest.mark.parametrize(
        'arguments',
        ExtractTotalAreaParams.formattings,
        ids=(
            "empty_text",
            "without_spaces",
            "with_lots_of_spaces",
            "only_with_square_value",
            "only_with_square_unit",
            "with_special_symbols_before_value",
            "with_special_symbols_instead_of_space",
            "with_several_square_units",
        ),
    )
    def test_check_formatting(self, arguments):
        description = """
            Тест проверяет, что текст некорректного формата ({}),
            конвертируется корректно в значение площади объекта.
            """
        allure.dynamic.title(arguments.test_title)
        allure.dynamic.description(description.format(arguments.test_desc))

        text = arguments.text
        expected_result = arguments.expected_result

        current_result = extract_total_area(text)
        assert current_result == expected_result

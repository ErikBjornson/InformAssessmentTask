import allure
import pytest

from src import split_num_and_text
from tests.split_num_and_text.parameters import SplitNumAndTextParams


@allure.epic("Выполнение тестового задания")
@allure.feature("Функция возврата цены и валюты объекта из текста")
@allure.story("Тестирование форматов вводимых цен и валют")
@pytest.mark.split_num_and_text
class TestSplitNumAndTextCheckingFormatting:
    """
    Класс с автотестами для проверки конвертации передаваемого
    в функцию ```split_num_and_text``` текста некорректного формата.
    """

    @pytest.mark.parametrize(
        'arguments',
        SplitNumAndTextParams.formattings,
        ids=(
            "empty_text",
            "without_spaces",
            "with_lots_of_spaces",
            "with_special_symbols_before_price",
            "with_special_symbols_instead_of_space",
            "with_special_symbols_in_currency",
            "without_price",
            "without_currency",
        ),
    )
    def test_check_formatting(self, arguments):
        description = """
            Тест проверяет, что текст некорректного формата ({}),
            корректно разделяется на значение цены объекта и валюту.
            """
        allure.dynamic.title(arguments.test_title)
        allure.dynamic.description(description.format(arguments.test_desc))

        text = arguments.text
        expected_result = arguments.expected_result

        current_result = split_num_and_text(text)
        assert current_result == expected_result

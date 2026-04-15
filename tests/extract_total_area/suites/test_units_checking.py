import allure
import pytest

from src.functions_for_testing import extract_total_area
from tests.extract_total_area.parameters import ExtractTotalAreaParams


@allure.epic("Выполнение тестового задания")
@allure.feature("Функция возврата площади объекта из текста")
@allure.story("Тестирование единиц измерения площадей")
@pytest.mark.extract_total_area
class TestExtractTotalAreaCheckingUnits:
    """
    Класс с автотестами для проверки корректности конвертации указываемых
    единиц измерения площадей, передаваемых в функцию ```extract_total_area```.
    """

    @pytest.mark.parametrize(
        'arguments',
        ExtractTotalAreaParams.units_checks,
        ids=(
            "with_m2_unit",
            "with_m_square_unit",
            "with_kv_point_m_unit",
            "with_kv_point_m_with_space_unit",
            "with_m_point_kv_unit",
            "with_m_point_kv_with_space_unit",
            "with_M2_unit",
            "with_M_square_unit",
            "with_ga_unit",
            "with_sot_unit",
            "with_sot_with_point_unit",
            "with_m3_unit",
            "with_square_miles_unit",
        ),
    )
    def test_check_convertation_for_different_units(self, arguments):
        description = """
            Тест проверяет корректность конвертации текста в площадь при
            указании значения площади {}.
            """
        allure.dynamic.title(arguments.test_title)
        allure.dynamic.description(description.format(arguments.test_desc))

        text = arguments.text
        expected_result = arguments.expected_result

        current_result = extract_total_area(text)
        assert current_result == expected_result

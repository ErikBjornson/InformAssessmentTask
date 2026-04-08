import re


def extract_total_area(text: str) -> float | None:
    """
    Возвращает площадь объекта из текста (в кв.м).
    Гектары конвертируются в сотки.
    """

    try:
        text = text.replace(",", ".")
        pattern = r"(\d+(\.\d+)?)\s*(м2|м²|кв\.м|м\.кв|га|сот\.)"

        match = re.search(pattern, text)

        if not match:
            return None

        value = float(match.group(1))
        unit = match.group(3)

        if unit == "га":
            value *= 100
        return value

    except Exception as e:
        print(f"extract_total_area: {e}")
        return None


def split_num_and_text(s: str) -> tuple[str | None, str | None]:
    """Возвращает цену и валюту объекта из текста."""

    price, units = None, None

    try:
        if s and isinstance(s, str):
            match = re.match(r"([\d\s]+)(.*)", s.replace("от", ""))
            if match:
                price = match.group(1).replace(" ", "")
                units = match.group(2).strip()
    except Exception as e:
        print(f"split_num_and_text: {e}")
    return price, units

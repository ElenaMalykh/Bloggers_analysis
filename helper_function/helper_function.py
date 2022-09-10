from dateutil import parser  # может разбирать даты


def get_year(input_date: str) -> int:
    return parser.parse(input_date).year


def get_month(input_date: str) -> int:
    return parser.parse(input_date).month


def get_blogger_category(input_str: str) -> str:
    return input_str[:input_str.find("_bloggers")]

def get_float_from_percent(input_string: str) -> float:
    return float(input_string
                 .strip('%')
                 .replace(',', '.'))
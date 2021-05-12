import re


def normalize_string(string: str) -> str:
    string = string.strip()
    string = re.sub("\s\s+", " ", string)

    return string

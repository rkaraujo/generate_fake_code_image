from src.config import *

def get_text_color(text):
    if text in DATA_TYPES:
        return COLOR_DATATYPE
    elif text in KEYWORDS:
        return COLOR_KEYWORD
    elif text in FUNCTIONS:
        return COLOR_FUNCTION
    elif text.startswith('"') and text.endswith('"'):
        return COLOR_STRING
    elif text.isdigit() or (text.startswith("0x") and all(c in "0123456789abcdefABCDEF" for c in text[2:])) or (text.startswith("0b") and all(c in "01" for c in text[2:])) or ('.' in text and text.replace('.', '').isdigit()):
        return COLOR_NUMBER
    elif text in OPERATORS:
        return COLOR_OPERATOR
    elif text in ["true", "false", "null"]:
        return COLOR_KEYWORD
    elif text.startswith("/*") and text.endswith("*/"):
        return COLOR_COMMENT
    elif text in ["(", ")", ",", ";"]:
        return COLOR_PUNCTUATION
    elif text in ["{", "}", "[", "]"]:
        return COLOR_BRACKET
    else:
        return COLOR_VARIABLE

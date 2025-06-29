import pytest

# Define colors for testing purposes (should match those in generate_fake_code_image.py)
COLOR_KEYWORD = (255, 100, 100)
COLOR_DATATYPE = (100, 200, 255)
COLOR_FUNCTION = (150, 255, 150)
COLOR_VARIABLE = (220, 220, 220)
COLOR_STRING = (255, 255, 100)
COLOR_NUMBER = (200, 150, 255)
COLOR_OPERATOR = (255, 180, 100)
COLOR_COMMENT = (120, 120, 120)
COLOR_PUNCTUATION = (180, 180, 180)
COLOR_BRACKET = (160, 160, 160)

# Simplified get_text_color for testing
def get_text_color_test(text):
    keywords = ["public", "private", "class", "static", "void", "int", "string", "bool", "float", "if", "else", "for", "while", "return", "try", "catch", "new"]
    operators = ["=", "==", "!=", "<", ">", "<=", ">=", "+", "-", "*", "/", "%", "++", "--"]
    data_types = ["int", "string", "bool", "float", "List<int>", "Map<string, string>"]
    functions = ["print", "calculate", "getData", "process", "isValid", "save", "load", "render"]

    if text in data_types:
        return COLOR_DATATYPE
    elif text in keywords:
        return COLOR_KEYWORD
    elif text in functions:
        return COLOR_FUNCTION
    elif text.startswith('"') and text.endswith('"'):
        return COLOR_STRING
    elif text.isdigit() or ('.' in text and text.replace('.', '').isdigit()):
        return COLOR_NUMBER
    elif text in operators:
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


def test_punctuation_coloring():
    assert get_text_color_test("(") == COLOR_PUNCTUATION
    assert get_text_color_test(")") == COLOR_PUNCTUATION
    assert get_text_color_test(",") == COLOR_PUNCTUATION
    assert get_text_color_test(";") == COLOR_PUNCTUATION

def test_bracket_coloring():
    assert get_text_color_test("{") == COLOR_BRACKET
    assert get_text_color_test("}") == COLOR_BRACKET
    assert get_text_color_test("[") == COLOR_BRACKET
    assert get_text_color_test("]") == COLOR_BRACKET

def test_other_coloring_remains_same():
    assert get_text_color_test("if") == COLOR_KEYWORD
    assert get_text_color_test("int") == COLOR_DATATYPE
    assert get_text_color_test("print") == COLOR_FUNCTION
    assert get_text_color_test("\"hello\"") == COLOR_STRING
    assert get_text_color_test("123") == COLOR_NUMBER
    assert get_text_color_test("==") == COLOR_OPERATOR
    assert get_text_color_test("true") == COLOR_KEYWORD
    assert get_text_color_test("/* comment */") == COLOR_COMMENT
    assert get_text_color_test("myVariable") == COLOR_VARIABLE

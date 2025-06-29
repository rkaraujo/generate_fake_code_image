import pytest
from src.syntax_highlighting import get_text_color
from src.config import *


def test_get_text_color_keyword():
    assert get_text_color("public") == COLOR_KEYWORD

def test_get_text_color_function():
    assert get_text_color("print") == COLOR_FUNCTION

def test_get_text_color_variable():
    assert get_text_color("my_var") == COLOR_VARIABLE

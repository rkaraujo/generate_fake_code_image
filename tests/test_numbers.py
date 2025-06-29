import pytest
import random

# Define colors for testing purposes (should match those in generate_fake_code_image.py)
COLOR_NUMBER = (200, 150, 255)

# Simplified get_text_color for testing (only relevant parts for numbers)
def get_text_color_test(text):
    if text.isdigit() or (text.startswith("0x") and all(c in "0123456789abcdefABCDEF" for c in text[2:])) or (text.startswith("0b") and all(c in "01" for c in text[2:])) or ('.' in text and text.replace('.', '').isdigit()):
        return COLOR_NUMBER
    else:
        return None # Or some other default color for non-numbers

# Mock generate_random_number_content function for testing
def generate_random_number_content_mock():
    num_type = random.choice(["int", "float", "hex", "bin"])
    if num_type == "int":
        return str(random.randint(0, 999))
    elif num_type == "float":
        return f"{random.uniform(0.0, 999.99):.2f}"
    elif num_type == "hex":
        return hex(random.randint(0, 255))
    elif num_type == "bin":
        return bin(random.randint(0, 255))


def test_numeric_type_generation_variety():
    generated_numbers = [generate_random_number_content_mock() for _ in range(1000)]
    
    has_int = False
    has_float = False
    has_hex = False
    has_bin = False

    for num_str in generated_numbers:
        if num_str.isdigit():
            has_int = True
        elif '.' in num_str and num_str.replace('.', '').isdigit():
            has_float = True
        elif num_str.startswith("0x"):
            has_hex = True
        elif num_str.startswith("0b"):
            has_bin = True
    
    assert has_int
    assert has_float
    assert has_hex
    assert has_bin

def test_get_text_color_for_numeric_types():
    assert get_text_color_test("123") == COLOR_NUMBER
    assert get_text_color_test("45.67") == COLOR_NUMBER
    assert get_text_color_test("0xAF") == COLOR_NUMBER
    assert get_text_color_test("0b101") == COLOR_NUMBER
    assert get_text_color_test("not_a_number") is None # Ensure it doesn't incorrectly color non-numbers

import pytest
import random

# Define colors for testing purposes (should match those in generate_fake_code_image.py)
COLOR_COMMENT = (120, 120, 120)
COLOR_PUNCTUATION = (180, 180, 180)
COLOR_BRACKET = (160, 160, 160)
COLOR_VARIABLE = (220, 220, 220)

# Simplified get_text_color for testing (only relevant parts for comments)
def get_text_color_test(text):
    if text.startswith("/*") and text.endswith("*/"):
        return COLOR_COMMENT
    elif text.startswith("//"):
        return COLOR_COMMENT
    elif text in ["(", ")", ",", ";"]:
        return COLOR_PUNCTUATION
    elif text in ["{", "}", "[", "]"]:
        return COLOR_BRACKET
    else:
        return COLOR_VARIABLE

# Mock generate_comment function for testing
def generate_comment_mock(comment_type_override=None):
    comment_type = comment_type_override if comment_type_override else random.choice(["single_line", "multi_line"])
    comment_text = random.choice(["This is a comment.", "TODO: Implement this.", "Fix bug #123.", "Important logic here."])
    if comment_type == "single_line":
        return [("//", COLOR_COMMENT), (comment_text, COLOR_COMMENT)]
    else:
        lines = [
            ("/*", COLOR_COMMENT),
            (" " * 4 + comment_text, COLOR_COMMENT),
            (" " * 4 + "More details...", COLOR_COMMENT),
            ("*/", COLOR_COMMENT)
        ]
        return lines


def test_get_text_color_single_line_comment():
    assert get_text_color_test("// This is a test") == COLOR_COMMENT

def test_get_text_color_multi_line_comment():
    assert get_text_color_test("/* This is a multi-line comment */") == COLOR_COMMENT

def test_generate_comment_single_line_format():
    random.seed(42) # for reproducibility
    comment_parts = generate_comment_mock()
    assert len(comment_parts) == 2
    assert comment_parts[0] == ("//", COLOR_COMMENT)
    assert comment_parts[1][1] == COLOR_COMMENT

def test_generate_comment_multi_line_format():
    comment_parts = generate_comment_mock(comment_type_override="multi_line")
    assert len(comment_parts) == 4
    assert comment_parts[0] == ("/*", COLOR_COMMENT)
    assert comment_parts[1][1] == COLOR_COMMENT
    assert comment_parts[2][1] == COLOR_COMMENT
    assert comment_parts[3] == ("*/", COLOR_COMMENT)

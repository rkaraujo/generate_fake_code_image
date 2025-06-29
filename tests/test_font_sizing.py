import pytest


# Mock ImageFont.truetype and ImageFont.load_default for testing
class MockImageFont:
    def __init__(self, size):
        self.size = size

    def getlength(self, text):
        # Simple mock: assume 8 pixels per character
        return len(text) * 8

    def getbbox(self, text):
        # Mock getbbox to return a dummy bounding box for textlength calculation
        return (0, 0, len(text) * 8, self.size)

# Mock the d.textlength method
class MockDraw:
    def textlength(self, text, font):
        return font.getlength(text)

# Extract the font sizing logic into a testable function
def calculate_optimal_font_size(width, height, num_statements):
    avg_chars_per_statement = 50  # A rough estimate
    estimated_total_chars = num_statements * avg_chars_per_statement

    estimated_lines = estimated_total_chars / (width / 8)  # Assuming 8 pixels per char width

    font_size = int(height / (estimated_lines + 2))  # +2 for some padding

    min_font_size = 10
    max_font_size = 24
    font_size = max(min_font_size, min(font_size, max_font_size))

    return font_size


def test_font_size_increases_with_height():
    font_size_small_height = calculate_optimal_font_size(1920, 540, 300)
    font_size_large_height = calculate_optimal_font_size(1920, 1080, 300)
    assert font_size_large_height >= font_size_small_height

def test_font_size_decreases_with_more_statements():
    font_size_few_statements = calculate_optimal_font_size(1920, 1080, 100)
    font_size_many_statements = calculate_optimal_font_size(1920, 1080, 500)
    assert font_size_few_statements >= font_size_many_statements

def test_font_size_stays_within_bounds():
    font_size_too_small = calculate_optimal_font_size(100, 100, 1000)
    font_size_too_large = calculate_optimal_font_size(5000, 5000, 10)
    assert font_size_too_small >= 10
    assert font_size_too_large <= 24

def test_font_size_with_edge_cases():
    # Very few statements, large image
    font_size = calculate_optimal_font_size(4000, 2000, 10)
    assert font_size == 24  # Should hit max_font_size

    # Many statements, small image
    font_size = calculate_optimal_font_size(800, 600, 1000)
    assert font_size == 10  # Should hit min_font_size

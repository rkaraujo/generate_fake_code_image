import pytest
from src.drawing import draw_code_on_image
import os


def test_draw_code_on_image():
    output_filename = "test_drawing.png"
    if os.path.exists(output_filename):
        os.remove(output_filename)

    draw_code_on_image([[("test", (255, 255, 255))]], 100, 100, output_filename)

    assert os.path.exists(output_filename)

    os.remove(output_filename)

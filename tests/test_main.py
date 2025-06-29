import pytest
from src.main import generate_fake_code
import os


def test_generate_fake_code_creates_file():
    """Tests if the generate_fake_code function creates an output file."""
    output_filename = "test_image.png"
    if os.path.exists(output_filename):
        os.remove(output_filename)

    generate_fake_code(output_filename=output_filename)

    assert os.path.exists(output_filename)

    os.remove(output_filename)
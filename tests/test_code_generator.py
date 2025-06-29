import pytest
from src.code_generator import generate_code_statements

def test_generate_code_statements():
    statements = generate_code_statements(10)
    assert len(statements) == 10

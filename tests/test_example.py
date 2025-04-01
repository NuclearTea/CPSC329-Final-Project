import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from logic.example_logic import example_function


def test_example_function():
    assert example_function() == "This is an example logic function."

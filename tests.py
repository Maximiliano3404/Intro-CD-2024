import pytest
import main as mn
from main import hello_world

def test_hello_world():
    assert mn.hello_world() is True
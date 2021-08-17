# test_sample.py

import pytest


@pytest.mark.parametrize("number", [1, 0])
def test_equal(number):
    assert number == 1


if __name__ == "__main__":
    pytest.main([])

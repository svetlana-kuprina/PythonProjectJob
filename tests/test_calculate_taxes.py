import pytest

from src.calculate_taxes import calculate_taxes

@pytest.mark.parametrize('prices, taxes, expected', [([100, 200, 300], 20, [120, 240, 360]), ([100, 200, 300], 30, [130, 260, 390])])

def test_calculate_taxes(prices, taxes, expected):
    assert calculate_taxes(prices, taxes) == expected

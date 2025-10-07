import pytest

from src.calculate_taxes import calculate_taxes

@pytest.mark.parametrize('price, tax_rate, expected', [([100, 200, 300], 20, [120, 240, 360]), ([100, 200, 300], 30, [130, 260, 390])])

def test_calculate_taxes(price, tax_rate, expected):
    assert calculate_taxes(price, tax_rate) == expected

def test_calculate_taxes_raises_error():
    with pytest.raises(ValueError) as excinfo:
        calculate_taxes([100, 200, 300], -10)
        assert str(excinfo) == ValueError("Неверный налоговый процент")

    with pytest.raises(ValueError) as exc_info:
        calculate_taxes([0, -10, 300], 10)
        assert str(excinfo) == ValueError("Неверная цена")

def calculate_tax(price: list[float], tax_rate: float) -> list[float]:
    """Функция вычисляет стоимость товаров с учётом налога."""

    if tax_rate < 0 or tax_rate >= 100:
        raise ValueError("Неверный налоговый процент")

    taxed_prices = []

    for pr in price:
        if pr <= 0:
            raise ValueError("Неверная цена")
        tax = pr * tax_rate / 100
        taxed_prices.append(pr + tax)

    return taxed_prices
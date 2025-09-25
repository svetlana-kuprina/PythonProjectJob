def sort_product(product: list, rev=False) -> list:
    """Функция сортировки продуктов"""

    new_product = sorted(product, reverse=rev)
    return new_product


print(sort_product([("banana", 3.5), ("apple", 2.5), ("orange", 1.5)], rev=True))

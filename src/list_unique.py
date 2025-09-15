def list_unique(mylist):
    """Функция возврящает список уникальных элементов"""
    return list(set(mylist))


print(list_unique([1, 2, 3, 4, 5, 6, 1]))

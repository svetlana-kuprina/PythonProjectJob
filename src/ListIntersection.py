from typing import Iterable


def list_intersection(list1: Iterable[int], list2: Iterable[int]) -> Iterable[int]:
    """функция, которая получает на вход два списка чисел и возвращает новый список, содержащий только те числа, которые встречаются в обоих списках."""

    intersection = set(list1).intersection(list2)
    return list(intersection)


print(list_intersection([1, 2, 3, 4, 5], [4, 5, 6, 7, 8, 9, 10]))

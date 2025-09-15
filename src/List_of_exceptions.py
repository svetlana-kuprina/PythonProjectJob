from typing import List


def get_list_of_exceptions(list_1: List[int], list_2: List[int]) -> list[int]:
    """Функция, которая получает на вход два списка чисел и возвращает новый список,
    содержащий только те числа, которые есть только в одном из списков"""
    list3 = set(list_1).difference(set(list_2))
    if list3 == set():
        list3 = set(list_2).difference(set(list_1))
    return list(list3)


print(get_list_of_exceptions([1, 2, 3], [1, 2, 3, 4, 5, 6, 7, 8]))

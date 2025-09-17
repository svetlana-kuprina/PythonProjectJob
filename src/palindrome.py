from typing import Iterable


def palindrome(string: Iterable[int]) -> Iterable[int]:
    """Функция возврящает список чисел которые являются палиндромами."""
    string_new = []

    for index in string:
        if str(index) == str(index)[::-1]:
            string_new.append(index)
    return string_new



print(palindrome([121, 212, 345, 4, 5]))

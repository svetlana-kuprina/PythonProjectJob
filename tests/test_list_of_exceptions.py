from src.List_of_exceptions import get_list_of_exceptions


def test_get_list_of_exceptions():
    assert get_list_of_exceptions([1, 2, 3], [1, 2, 3, 4, 5, 6, 7, 8]) == [4, 5, 6, 7, 8]
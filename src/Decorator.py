import time
from functools import wraps


def dek_numbers(func):
    """Функция декоратор которая проверяет, что все числа, возвращаемые декорируемой функцией, являются целыми,
     и округляет их до целых, если это не так"""

    def wrapper(*args, **kwargs):
        function = func(*args, **kwargs)
        if type(function) == float:
            return round(function)
        elif type(function) in (list, tuple):
            rounded = [round(x) if type(x) == float else x for x in function]
            return type(function)(rounded)
        else:
            return function

    return wrapper


if __name__ == '__main__':
    @dek_numbers
    def number(b):
        return b


    print(number([5, 1, 25, 55.55, 6.5]))


def dek_error(func):
    """декоратор, который повторно вызывает декорируемую функцию три раза. Каждый раз через три секунды, если произошла ошибка."""

    def wrapper(*args, **kwargs):
        for x in range(3):
            try:
                return func(*args, **kwargs)
            except Exception:
                time.sleep(3)
        return Exception('Ошибка работы функции')

    return wrapper


def dek_yield(func):
    """Декоратор, который позволяет возвращать элементы декорируемой функции по одному через yield,
     если эта функция возвращает список или кортеж."""

    def wrapper(*args, **kwargs):
        function = func(*args, **kwargs)
        if type(function) in (list, tuple):
            for item in function:
                yield item
        else:
            yield function

    return wrapper


def dek_text_abbreviation(func):
    """Декоратор, который берет результат декорируемой функции (текст) и возвращает текст,
    в котором каждое слово сокращено до 8 символов. Если слово было сокращено, в конце слова ставится точка"""

    def wrapper(test: str):
        function = func(test)
        function_split = function.split()
        function_text = ''
        for item in function_split:
            if len(item) > 8:
                function_text += item[0:8] + '.' + ' '
            else:
                function_text += item + ' '
        return function_text

    return wrapper


if __name__ == '__main__':
    @dek_text_abbreviation
    def text_output(test: str):
        return test

print(text_output('Привет я хочу много гулляяяяяять очень многоооооого'))


def dek_exclamation_mark(func):
    """декоратор должен заменять в тексте, который выдает функция '!' """

    def wrapper(test: str):
        function = func(test)
        return function.replace("!", "!!!")

    return wrapper


def dek_question_mark(func):
    """декоратор должен заменять в тексте, который выдает функция '?' """

    def wrapper(test: str):
        function = func(test)
        return function.replace("?", "???")

    return wrapper


def dek_period_mark(func):
    """декоратор должен заменять в тексте, который выдает функция '.' """

    def wrapper(test: str):
        function = func(test)
        return function.replace(".", "...")

    return wrapper


if __name__ == '__main__':
    @dek_period_mark
    @dek_question_mark
    @dek_exclamation_mark
    def exclamation_mark(test: str):
        return test


    print(exclamation_mark("Привет. я хочу много гулляяяяяять очень многоооооого! Точно?"))


def dek_numbers_round(precision):
    """декоратор, который проверяет, что все числа, возвращаемые декорируемой функцией, являются целыми, и округляет их
     до целых, если это не так. Декоратор принимает параметр, который указывает, до скольких цифр после запятой округлять числа."""

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            function = func(*args, **kwargs)
            if type(function) == float:
                return round(function, precision)
            elif type(function) in (list, tuple):
                rounded = [round(x, precision) if type(x) == float else x for x in function]
                return type(function)(rounded)
            else:
                return function

        return inner

    return wrapper


if __name__ == '__main__':
    @dek_numbers_round(0)
    def number(b):
        return b


    print(number((5, 1, 25, 55.55, 6.5)))


def dec_error_param(*, retries=3, delay=3):
    """декоратор, который повторно вызывает декорируемую функцию заданное количество раз через заданное время, если произошла ошибка"""

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            for x in range(retries):
                try:
                    function = func(*args, **kwargs)
                    return function
                except Exception:
                    time.sleep(delay)
                return Exception('Ошибка работы функции')

        return inner

    return wrapper



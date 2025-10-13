
def dek(func):
    def wrapper(*args, **kwargs):
        function = func(*args, **kwargs)
        if function % 2 != 0:
            return round(function, 0)
    return wrapper

@dek
def namber(b:int):
    return b

print(namber(5))
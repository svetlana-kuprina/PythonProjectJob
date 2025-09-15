def get_below_average(list_n):
    """Функция вывода значений меньше среднего"""
    new_list = []
    sr = sum(list_n) / int(len(list_n))
    for i in list_n:
        if i < sr:
            new_list.append(i)

    return print(new_list)


get_below_average([1, 2, 3, 4, 5])

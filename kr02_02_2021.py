def task_1(two_dim_words):
    two_dim_words = [["корова", "овечка", "коза"], ["гусь", "цыпленок", "курица"]]
    sorted_words = []
    for i in range(len(two_dim_words)):
        sorted_words.extend(two_dim_words[i])
    sorted_words.sort(key=len and str.upper)
    print(sorted_words)
    return sorted_words


def task_3(numbers):
    """
        Здесь должен быть ваш код.
        Переменная numbers - ваша строка чисел.
        Финальное значение должно быть помещено в переменную dict_min.
        """

    pass


def task_4_1(words):
    """
        Здесь должен быть ваш код.
        Переменная words - ваш кортеж слов из задания.
        Финальное значение должно быть помещено в переменную res.
        """

    pass


def task_4_2(words):  # можно сделать тесты
    """
        Здесь должен быть ваш код.
        Переменная words - ваш кортеж слов из задания.
        Финальное значение должно быть помещено в переменную res.
        """

    pass


def task_4_3(words):
    """
        Здесь должен быть ваш код.
        Переменная words - ваш кортеж слов из задания.
        Финальное значение должно быть помещено в переменную res.
        """

    pass


def task_5(lst1, lst2):
    lst1 = [1, 4, 7, 5, 8]
    lst2 = [1, 3, 8, 4, 3]
    diff = []
    set2 = set(lst2)
    for i in range(len(lst1)):
        if lst1[i] not in set2:
            diff.extend(str(lst1[i]))
        else:
            continue
    print(sorted(diff))
    return diff


def task_6(lst):
    """
        Здесь должен быть ваш код.
        Переменная lst - ваш список.
        Финальное значение должно быть помещено в переменную res.
        """

    pass


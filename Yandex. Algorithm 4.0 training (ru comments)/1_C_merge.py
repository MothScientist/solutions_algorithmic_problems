# C. Слияние

# Ограничение времени: 5 секунд
# Ограничение памяти: 512Mb

# Ввод: стандартный ввод или input.txt.txt
# Вывод: стандартный вывод или output.txt
# Базовый алгоритм для сортировки слиянием — алгоритм слияния двух упорядоченных массивов в один упорядоченный массив.
# Эта операция выполняется за линейное время с линейным потреблением памяти.
# Реализуйте слияние двух массивов в качестве первого шага для написания сортировки слиянием.

# Формат ввода:
# В первой строке входного файла содержится число N — количество элементов первого массива (0 ≤ N ≤ 106).
# Во второй строке содержатся N целых чисел ai, разделенных пробелами, отсортированные по неубыванию (-109 ≤ ai ≤ 109).
# В третьей строке входного файла содержится число M — количество элементов второго массива (0 ≤ M ≤ 106).
# В третьей строке содержатся M целых чисел bi, разделенных пробелами, отсортированные по неубыванию (-109 ≤ bi ≤ 109).
#
# Формат вывода:
# Выведите результат слияния этих двух массивов, то есть M + N целых чисел, разделенных пробелами, в порядке неубывания.

# Пример 1
# Ввод:
# 5
# 1 3 5 5 9
# 3
# 2 5 6
# Вывод:
# 1 2 3 5 5 5 6 9

# Пример 2
# Ввод:
# 1
# 0
# 0
#
# Вывод:
# 0

# Пример 3
# Ввод:
# 0
#
# 1
# 0
# Вывод:
# 0

# Примечания:
# Для решения этой задачи советуем реализовать функцию, которая принимает на вход две пары итераторов,
# задающие два массива, и итератор на начало буфера, в который необходимо записывать результат.
# Итераторы можно заменить на передачу массивов и индексов в них.
# В таком виде вам будет удобно использовать эту функцию для реализации сортировки.

def merge_sort(_a, _b, a_len, b_len):
    a_cur = 0
    b_cur = 0
    _res = []

    while a_cur < a_len and b_cur < b_len:
        if _a[a_cur] <= _b[b_cur]:
            _res.append(_a[a_cur])
            a_cur += 1
        else:
            _res.append(_b[b_cur])
            b_cur += 1

    _res += _a[a_cur:] + _b[b_cur:]

    return _res


a_n = int(input())
a = list(map(int, input().split()))  # map даёт выигрыш во времени

b_n = int(input())
b = list(map(int, input().split()))  # здесь аналогично

res = merge_sort(a, b, a_n, b_n)

res_str = " ".join(map(str, res))  # тут тоже join и map позволяют вытащить пару секунд
print(res_str)
# H. Результаты контеста
#
# Ограничение времени: 1 секунда
# Ограничение памяти: 64Mb
# Ввод	стандартный ввод или input.txt.txt
# Вывод	стандартный вывод или output.txt

# Чтобы оценить качество обучения программированию,
# в каждой группы студентов подсчитывается один параметр — суммарное количество решенных студентами задач.
#
# Известно, что в первой группе суммарное количество решенных на контесте задач равно a, а во второй — b.
# Всего на контесте было предложено n задач,
# а также известно, что каждый студент решил не менее одной (и не более n) задач.
#
# По заданным a, b и n определите, могло ли в первой группе быть строго больше студентов, чем во второй.
#
# Формат ввода:
# Вводятся три целых числа a, b, n (1 ≤ a, b, n ≤ 10000).
#
# Формат вывода:
# Выведите "Yes" если в первой группе могло быть строго больше студентов, чем во второй, и "No" в противном случае.
#
# Пример 1
# Ввод:
# 60
# 30
# 4
# Вывод:
# Yes

# Пример 2
# Ввод:
# 30
# 30
# 1
# Вывод:
# No

# Пример 3
# Ввод:
# 30
# 150
# 4
# Вывод:
# No

def solution(a_s, b_s, count):
    b_min = b_s // count + 1 if b_s % count != 0 else b_s // count

    if a_s > b_min:
        return "Yes"
    else:
        return "No"


a = int(input())
b = int(input())
n = int(input())

print(solution(a, b, n))

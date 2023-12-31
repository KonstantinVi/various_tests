# Условие задачи
#
# Ограничение времени, с	1
# Ограничение памяти, МБ	64
# Общее число попыток отправки	15
#
# Разработчик Фёдор очень любит печеньки в офисе, и он точно знает все N мест, где их можно найти,
# а также точное количество печенек Сn в каждом месте. Сегодня Фёдор особенно голоден,
# он закончил большую задачу, и решает выделить себе M часов на то, чтобы съесть все печеньки в офисе.
#
# Фёдор рассчитал минимальное количество печенек K, которое ему нужно съедать в течение часа так,
# чтобы в итоге успеть съесть все печеньки в офисе за выделенное время.
#
# В каждый час, он может посетить одно любое место с печеньками и съесть K печенек в этом месте,
# он потратит на это целый час, даже если в этом месте осталось меньше, чем K печенек, потому что
# будет обсуждать с коллегами задачи и планы. Места без печенек Фёдор может не посещать.
#
# Коллеги, из уважения к Фёдору, никогда не трогают его любимые печеньки.
#
#
# Входные данные (поступают в стандартный поток ввода)
# Первая строка - целые числа N и M через пробел (1≤N≤100 000, 1≤M≤200 000)
#
# Далее N строк, на каждой из которых одно целое число Cn (0≤Cn≤10 000)
#
# Все входные данные наших тестов всегда соблюдают указанные параметры, дополнительные проверки не требуются
#
#
# Выходные данные (ожидаются в стандартном потоке вывода)
# Одно целое число, минимально возможное K, либо 0, если Фёдор не успеет съесть все печеньки
#
#
# Пример 1
#
# Ввод:
# 3 6
# 4
# 4
# 4
#
# Вывод:
# 2
#
# Простой пример для ознакомления с входными и выходными данными
#
#
# Пример 2
#
# Ввод:
# 3 6
# 4
# 4
# 5
#
# Вывод:
# 3
#
# Здесь похожая ситуация, но съедая по 2 печеньки, Фёдор не успеет съесть последнюю
#
#
# Пример 3
#
# Ввод:
# 3 3
# 6
# 6
# 8
#
# Вывод:
# 8
#
# Граничная ситуация при N = M


# РЕШЕНИЕ
def fedor_cookies(n: int, m: int, arr: tuple) -> int:
    """Фёдор и печеньки\n
    :argument
        + n - количество точек
        + m - количество часов
        + arr - количество печенек в точках"""
    if n > m:
        return 0
    if n == m:
        return max(arr)
    if n < m:
        _one_val = 1
        _two_val = max(arr)
        while _one_val <= _two_val:
            median = (_one_val + _two_val) // 2
            hours_needed = sum(
                [c // median + (1 if c % median else 0) for c in arr])

            if hours_needed <= m:
                _two_val = median - 1
            else:
                _one_val = median + 1

        return _one_val if _one_val <= max(arr) else 0


n, m = map(int, (input().split()))
arr = [int(input()) for _ in range(n)]
arr.sort(reverse=True)
arr = tuple(arr)
print(fedor_cookies(n, m, arr))

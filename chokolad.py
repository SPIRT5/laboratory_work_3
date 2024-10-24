def min_breaks(n, m):
    # Если шоколадка уже состоит из одного квадратика
    if n == 1 and m == 1:
        return 0
    # Общее количество разломов
    return n * m - 1

# Проверка примеров
print(min_breaks(2, 3))  # Ожидается 5
print(min_breaks(3, 3))  # Ожидается 8
print(min_breaks(3, 5))  # Ожидается 14
print(min_breaks(1, 1))  # Ожидается 0
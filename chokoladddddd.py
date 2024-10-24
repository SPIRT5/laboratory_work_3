def min_breaks(n, m, memo=None):
    if memo is None:
        memo = {}
    
    # Базовый случай: если шоколадка уже состоит из одного квадратика
    if n == 1 and m == 1:
        return 0
    
    # Если результат уже был вычислен, возвращаем его из кэша
    if (n, m) in memo:
        return memo[(n, m)]
    
    # Попробуем сделать разломы по горизонтали и вертикали
    min_breaks_result = float('inf')
    
    # Горизонтальные разломы
    for i in range(1, n):
        top_part = min_breaks(i, m, memo)
        bottom_part = min_breaks(n - i, m, memo)
        min_breaks_result = min(min_breaks_result, top_part + bottom_part + 1)
    
    # Вертикальные разломы
    for j in range(1, m):
        left_part = min_breaks(n, j, memo)
        right_part = min_breaks(n, m - j, memo)
        min_breaks_result = min(min_breaks_result, left_part + right_part + 1)
    
    # Запоминаем результат для текущего n и m
    memo[(n, m)] = min_breaks_result
    return min_breaks_result

# Проверка примеров
print(min_breaks(2, 3))  # Ожидается 5
print(min_breaks(3, 3))  # Ожидается 8
print(min_breaks(1, 1))  # Ожидается 0
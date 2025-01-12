def get_matrix(n, m, value):
    # Создаем пустой список для матрицы
    matrix = []
    # Внешний цикл для строк
    for i in range(n):
        # Создаем пустой список для строки
        row = []
        # Внутренний цикл для столбцов
        for j in range(m):
            # Заполняем строку значениями value
            row.append(value)
        # Добавляем заполненную строку в матрицу
        matrix.append(row)
    # Возвращаем созданную матрицу
    return matrix
print(get_matrix(2, 2, 10))
print(get_matrix(3, 5, 42))
print(get_matrix(4, 2, 13))
# Задача 36: 
# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру 
# строки и столбца. Аргументы num_rows и num_columns указывают число строк и 
# столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов 
# идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией 
# называется любая операция, у которой ровно два аргумента, как, например, 
# у операции умножения.
# *Пример:*
# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

#Далее вывод с помощью матрицы:
def create_matrix(matrix, x, y):
    for i in range(x + 1):
        matrix.append([0] * (y+ 1))

def fill_matrix(matrix, operation, x, y):
    for x in range(1, x + 1):
        for y in range(1, y + 1):
            matrix[x][y] = operation(x, y)

def print_matrix(matrix):
    for i in range(1, len(matrix)):         
        for j in range(1, len(matrix[i])):
            print(matrix[i][j],'\t', end = ' ')
        print()      

#А тут вывод как в примере, не смог придумать/загуглить, как сюда включить табуляцию:
def print_operation_table(operation, x, y):
    for x in range (1, x + 1): 
        def_list1 = []
        for y in range (1, y + 1):
            def_list1.append(operation(x, y))
        print(*def_list1)

x = int(input('Insert number of rows: '))
y = int(input('Insert number of columns: '))

matrix = []

print_operation_table(lambda x, y: x * y, x, y)
print()
create_matrix(matrix, x,y)
fill_matrix(matrix, lambda x, y: x * y, x, y)
print_matrix(matrix)



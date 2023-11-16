#Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n

def print_multiplication_table(n):
    result = '\n'.join(f'{i} * {j} = {i * j}' for i in range(1, n+1) for j in range(1, n+1))
    print(result)

print_multiplication_table(10)
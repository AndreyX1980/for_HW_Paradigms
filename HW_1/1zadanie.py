# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

def sort_list_imperative(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

if __name__ == '__main__':
    nums = [8, 4, 9, 5, 10, 1, 2]
    print(sort_list_imperative(nums))
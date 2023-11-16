# Дан список целых чисел numbers. Необходимо написать в декларативном стиле процедуру для
# сортировки числа в списке в порядке убывания.

def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)


if __name__ == '__main__':
    nums = [8, 4, 9, 5, 10, 1, 2]
    print(sort_list_declarative(nums))
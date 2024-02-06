def count_of_numbers(nums):
    nums = list(set(nums))
    return len(nums)

numebrs1 = [1, 2, 3, 2, 1]
numbers2 = [1, 2, 3, 4, 5, 6, 7]
numbers3 = [1, 1, 1, 1, 1]
numbers4 = [1, 2, 3, 1, 1]

print(count_of_numbers(numebrs1))
print(count_of_numbers(numbers2))
print(count_of_numbers(numbers3))
print(count_of_numbers(numbers4))
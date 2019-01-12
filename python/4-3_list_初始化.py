nums = list(range(1, 1000001))
print('min:' + str(min(nums)))
print('max:' + str(max(nums)))
print('sum:' + str(sum(nums)) + '\n')

nums = list(range(1, 21, 2))
for num in nums:  # num不是引用，通过修改num无法修改nums的元素
    print(num)
print('\n')

nums = list(range(3, 31, 3))
print(nums)
print('\n')

nums = [i**3 for i in range(1, 11)]
print(nums)
print('\n')

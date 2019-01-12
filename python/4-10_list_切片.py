nums = list(range(1, 31))

nums_copy_deep = nums  # 两个list是相同的
nums_copy_shallow = nums[:]  # 两个list是不同的

nums.append(31)
nums_copy_shallow.pop()

print(nums)
print(nums_copy_shallow)
print(nums[-10:-5])  # 切片中使用的下标是index

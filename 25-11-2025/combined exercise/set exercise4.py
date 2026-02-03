nums= {2, 4, 6, 8, 10}
target = 12
pairs = []
nums = list(nums)
for i in range(len(nums)):
    for j in range(i, len(nums)):
        if nums[i] + nums[j] == target:
            pairs.append((nums[i], nums[j]))
print(pairs)
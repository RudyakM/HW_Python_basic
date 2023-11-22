def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                return[i, j]
            
result = twoSum(nums = [2,7,11,15], target = 9)
print(result)
result = twoSum(nums = [3,2,4], target = 6)
print(result)
result = twoSum(nums = [3,3], target = 6)
print(result)
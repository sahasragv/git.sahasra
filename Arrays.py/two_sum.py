# Given an array nums and integer target, return indices of two numbers
# such that they add up to target.
# Example:
# nums = [2,7,11,15], target = 9
# Output: [0,1]

# Code:

nums = [2, 7, 11, 15]
target = 9


def twosum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i, j]


print(twosum(nums, target))

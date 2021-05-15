def twoSum(nums: list, target: int):
    """
    Given an array of integers nums and an integer target, return indices of
    the two numbers such that they add up to target.You may assume that each
    input would have exactly one solution,and you may not use the same element
    twice. You can return the answer in any order.

    >>> twoSum([3, 2, 1, 4], 6)
    [1, 3]
    """
    dic = {i: target - nums[i] for i in range(len(nums))}
    for i in dic:
        if dic[i] in nums and nums.index(dic[i]) != i:
            return [i, nums.index(dic[i])]

    """
    for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums:
                if nums.index(diff) != i:
                    return [i, nums.index(target - nums[i])]
    """

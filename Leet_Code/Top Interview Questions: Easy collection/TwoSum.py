class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_nums = {}
        for i in range(0,len(nums)):
            if nums[i] not in dict_nums:
                dict_nums[nums[i]] = [i]
            else:
                dict_nums[nums[i]].append(i)
        for i in range(0, len(nums)):
            if target - nums[i] in dict_nums:
                if target - nums[i] == nums[i]:
                    if len(dict_nums[nums[i]]) > 1:
                        return [dict_nums[nums[i]][0],dict_nums[nums[i]][1]]
                else:
                    return [dict_nums[nums[i]][0],dict_nums[target-nums[i]][0]]
"""
63 / 63 test cases passed.
Status: Accepted
Runtime: 39 ms
Memory Usage: 13.5 MB
time complexity: O(n)
"""


"""
 for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            return [i,j]

time complexity: O(n^2)
"""
                
    
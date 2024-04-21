class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)
        return nums
"""
74 / 74 test cases passed.
Status: Accepted
Runtime: 699 ms
Memory Usage: 12.9 MB
"""

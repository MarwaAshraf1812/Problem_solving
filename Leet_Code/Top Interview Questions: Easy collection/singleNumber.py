class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict_nums = {}
        for i in nums:
            if i not in dict_nums:
                dict_nums[i] = 1
            else:
                dict_nums[i] += 1
        for i in dict_nums:
            # frequancy of the number is 1 return it
            if dict_nums[i] == 1:
                return i

        # nums = sorted(nums)
        # for i in range(1, len(nums)):
        #     if nums[i] != nums[i - 1]:
        #         return nums[i]
            
"""
61 / 61 test cases passed.
Status: Accepted
Runtime: 99 ms
Memory Usage: 14.5 MB
"""
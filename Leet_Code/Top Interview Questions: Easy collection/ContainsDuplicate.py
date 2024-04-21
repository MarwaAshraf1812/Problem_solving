class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        j = 0
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[j]:
                return True
            j += 1
        return False
    """
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i  - 1]:
                return True
        return False
        
        
        check if the number is in the dict IF yes return True
        else return assign the number to the dict
        dict_nums = {}
        for i in nums:
            if i in dict_nums:
                return True
            dict_nums[i] = 1
        return False
        
    """

"""
75 / 75 test cases passed.
Status: Accepted
Runtime: 447 ms
Memory Usage: 22 MB
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        for i in range(0, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j + 1

# 362 / 362 test cases passed.
# Status: Accepted
# Runtime: 59 ms
# Memory Usage: 13.5 MB
# Submitted: 0 minutes ago

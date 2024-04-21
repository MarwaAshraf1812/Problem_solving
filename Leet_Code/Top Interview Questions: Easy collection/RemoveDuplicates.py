class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # j = 0
        # for i in range(0, len(nums)):
        #     if nums[i] != nums[j]:
        #         j += 1
        #         nums[j] = nums[i]
        # # return k  len of new array 
        # return j + 1

        """ 
        set() removes duplicates but didnt return new array length
        but we(eslam ana marwa :)) can do a hack to using set to remove duplicates
        and then sort the set and itrate on it and replace the
        items to the original array and return the length of the
        array
        """
        unique = set(nums)
        count = 0
        unique = sorted(unique)
        for i in unique:
            nums[count] = i
            count += 1
        return count

# 362 / 362 test cases passed.
# Status: Accepted
# Runtime: 59 ms
# Memory Usage: 13.5 MB
# Submitted: 0 minutes ago

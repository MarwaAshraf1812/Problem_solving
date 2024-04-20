class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # ensures that the number of rotations does not exceed the length of the array.
        k %= n
        # The last k elements are moved to the front of the array.
        nums[:] = nums[-k:] + nums[:-k]
        return nums
    
"""
nums[-k:]: This slice takes the last k elements of the array.
nums[:-k]: This slice takes all elements from the start of the array up to the n-kth element.
and conatenates them to form the new array.

note :
The reverse method does not require extra space proportional to the size of the input list, as it operates directly on the original array through element swaps.

38 / 38 test cases passed.
Status: Accepted
Runtime: 132 ms
Memory Usage: 23 MB
"""
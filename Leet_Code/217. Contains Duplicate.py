"""
    Day 1:
    This implementation uses a set to efficiently keep track of 
    unique elements encountered during the iteration. If a duplicate is found, 
    the method returns True; otherwise, it returns False. The time complexity of this solution is O(n),
    where n is the length of the input array nums, 
    due to the constant-time average complexity of set operations like in and add.
"""
class Solution(object):
    def containsDuplicate(self, nums):
        un_set = set()
        for i in nums:
            if i in un_set: return True
            else: un_set.add(i)
        return False


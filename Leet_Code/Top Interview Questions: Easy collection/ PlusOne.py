class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        convert = str(int(''.join(map(str, digits))) + 1)
        new = [int(i) for i in convert]
        return new
    
"""
111 / 111 test cases passed.
Status: Accepted
Runtime: 14 ms
Memory Usage: 11.7 MB
"""
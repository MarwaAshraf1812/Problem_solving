class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict_1 = {}
        dict_2 = {}
        for i in nums1:
            if i not in dict_1:
                dict_1[i] = 1
            else:
                dict_1[i] += 1
        

        """
        answer = []
        for i in range(0, len(nums1)):
            if nums1[i] in nums2:
                answer.append(nums1[i])
                nums2.remove(nums1[i])
        return answer
        """
    
"""
57 / 57 test cases passed.
Status: Accepted
Runtime: 33 ms
Memory Usage: 11.7 MB
"""
        
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        answer = []
        for i in range(0, len(nums1)):
            if nums1[i] in nums2:
                answer.append(nums1[i])
                nums2.remove(nums1[i])
        return answer

        """
        set_1 = Multiset(nums1)
        set_2 = Multiset(nums2)
        set_3 = set_1.intersection(set_2)
        return set_3
        """
"""
57 / 57 test cases passed.
Status: Accepted
Runtime: 33 ms
Memory Usage: 11.7 MB
"""
        
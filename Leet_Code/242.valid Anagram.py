"""
This implementation checks if two strings 
are anagrams by sorting their characters and 
comparing the sorted versions. 
If the sorted versions are equal, 
the strings are considered anagrams, and
the method returns True. 
Otherwise, it returns False.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted =sorted(s)
        t_sorted = sorted(t)
        return True if s_sorted == t_sorted else False
        
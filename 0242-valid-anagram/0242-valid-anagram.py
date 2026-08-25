class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
'''class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = sorted(s) == sorted(t)
        print(result)
        return result
'''
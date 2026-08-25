class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for char in t:
            if char not in count:
                return False

            count[char] -= 1

        return all(x == 0 for x in count.values())

'''class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = sorted(s) == sorted(t)
        print(result)
        return result
'''
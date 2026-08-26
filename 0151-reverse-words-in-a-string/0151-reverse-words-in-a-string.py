class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ""

        for c in s:
            if c != " ":
                word += c
            elif word:
                words.append(word)
                word = ""

        if word:
            words.append(word)

        result = ""

        for i in range(len(words) - 1, -1, -1):
            result += words[i]
            if i != 0:
                result += " "

        return result
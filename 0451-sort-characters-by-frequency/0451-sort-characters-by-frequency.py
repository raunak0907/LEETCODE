class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1

        result = ""

        while count:
            max_char = ""
            max_freq = 0

            for c in count:
                if count[c] > max_freq:
                    max_freq = count[c]
                    max_char = c

            result += max_char * max_freq
            del count[max_char]

        return result
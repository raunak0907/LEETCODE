class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"

        for _ in range(n - 1):
            new = ""
            i = 0

            while i < len(result):
                count = 1

                # Count consecutive identical characters
                while i + 1 < len(result) and result[i] == result[i + 1]:
                    count += 1
                    i += 1

                # Append the count and the character to the new string
                new += str(count) + result[i]
                i += 1  # Move to the next unique character

            result = new

        return result
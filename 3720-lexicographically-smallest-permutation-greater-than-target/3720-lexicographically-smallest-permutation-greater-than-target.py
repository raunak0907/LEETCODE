class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord('a')] += 1

        ans = []

        for i in range(len(target)):
            x = ord(target[i]) - ord('a')

            # Try equal character
            if count[x] > 0:
                count[x] -= 1
                ans.append(target[i])
                continue

            # Try a character greater than target[i]
            for j in range(x + 1, 26):
                if count[j] > 0:
                    count[j] -= 1

                    result = ''.join(ans)
                    result += chr(j + ord('a'))

                    for k in range(26):
                        result += chr(k + ord('a')) * count[k]

                    return result

            # If nothing greater, backtrack
            break

        # Backtrack through previous characters
        for i in range(len(ans) - 1, -1, -1):
            x = ord(ans[i]) - ord('a')
            count[x] += 1
            ans.pop()

            for j in range(x + 1, 26):
                if count[j] > 0:
                    count[j] -= 1

                    result = ''.join(ans)
                    result += chr(j + ord('a'))

                    for k in range(26):
                        result += chr(k + ord('a')) * count[k]

                    return result

        return ""
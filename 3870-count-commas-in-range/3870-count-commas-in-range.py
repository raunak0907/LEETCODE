class Solution:
    def countCommas(self, n: int) -> int:
        commas = 0
        power = 1000
        group = 1

        while power <= n:
            commas += (n - power + 1) * group
            power *= 1000
            group += 1

        return commas
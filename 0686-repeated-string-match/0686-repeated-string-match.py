class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # 1. Find how many times 'a' completely fits into 'b'
        n = len(b) // len(a)
        
        # 2. If there is a remainder, we need one extra copy to cover the spillover
        if len(b) % len(a) != 0:
            n += 1
            
        # Build the initial repeated string
        s = a * n
        
        # Check the baseline, +1, and +2 copies
        if b in s:
            return n
            
        if b in s + a:
            return n + 1
            
        if b in s + a + a:
            return n + 2
            
        return -1
from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        if len(target) != n:
            return ""

        counts = Counter(s)
        odd_count = 0
        mid_char = ""
        
        for char, cnt in counts.items():
            if cnt % 2 != 0:
                odd_count += 1
                mid_char = char
                
        if odd_count > 1:
            return ""
            
        avail = {c: cnt // 2 for c, cnt in counts.items() if cnt // 2 > 0}
        k = n // 2
        
        rem_avail = {c: avail.get(c, 0) for c in 'abcdefghijklmnopqrstuvwxyz'}
        max_i = 0
        
        for i in range(k):
            c = target[i]
            if rem_avail.get(c, 0) > 0:
                rem_avail[c] -= 1
                max_i = i + 1
            else:
                break
                
        if max_i == k:
            H = target[:k]
            P = H + mid_char + H[::-1]
            if P > target:
                return P
                
        start_i = min(max_i, k - 1)
        
        if max_i == k and k > 0:
            rem_avail[target[k-1]] += 1
            
        for i in range(start_i, -1, -1):
            best_c = None
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c > target[i] and rem_avail[c] > 0:
                    best_c = c
                    break
                    
            if best_c:
                rem_avail[best_c] -= 1
                
                tail = []
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    tail.append(c * rem_avail[c])
                    
                H = target[:i] + best_c + "".join(tail)
                P = H + mid_char + H[::-1]
                return P
                
            if i > 0:
                rem_avail[target[i-1]] += 1
                
        return ""
class Solution:
    def myAtoi(self, s: str) -> int:
        n=len(s)
        i=0
        while i<n and s[i]==" ":
            i+=1
        sign=1
        if i<n and s[i]=="-":
            i+=1
            sign=-1
        elif i<n and s[i]=="+":
            i+=1
        num=0
        while i<n and '0'<=s[i]<='9':
            num=num*10+(ord(s[i])-ord('0'))
            i+=1
        num*=sign
        if num<-2**31:
            return -2**31
        if num>2**31-1:
            return 2**31-1
        return num
        
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        count={}
        for num in nums:
            count[num]=count.get(num,0)+1
        res=[]
        for num in count:
            if count[num]>len(nums)//3:
                res.append(num)
        return res
        
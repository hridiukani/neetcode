class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_dup=nums.copy()
        res=[]
        mult=1
        for i in nums:
            nums_dup.remove(i)
            for j in nums_dup:
                mult*=j
            nums_dup=nums.copy()
            res.append(mult)
            mult=1
        return res
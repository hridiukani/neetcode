class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        prod=1
        count=0
        for i in nums:
            if i==0:
                count+=1
            else:
                prod*=i
        
        if count>1:
            return res
        
        for i in range(len(nums)):
            if count:
                if nums[i]==0:
                    res[i]=prod
                
            else:
                res[i]=prod//nums[i]
        
        return res
        res = [0] * len(nums)

        
        
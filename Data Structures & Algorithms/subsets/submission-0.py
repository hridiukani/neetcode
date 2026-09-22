class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        
    
        def backtrack(nums, start, current, result):
            result.append(list(current))

            for i in range(start,len(nums)):
                current.append(nums[i])
                backtrack(nums,i+1,current,result)
                current.pop()

        backtrack(nums,0,[],result)
        return result
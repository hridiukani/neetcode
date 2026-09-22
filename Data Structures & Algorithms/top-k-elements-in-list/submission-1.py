class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=defaultdict()
        for i in nums:
            res[i]=nums.count(i)
        ans=[]
        for i in res:
            if res.get(i)>=k:
                ans.append(i)

        return ans

        
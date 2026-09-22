class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count=set()
        for i in nums:
            count.add(i)

        if len(count)<len(nums):
            return True
        return False

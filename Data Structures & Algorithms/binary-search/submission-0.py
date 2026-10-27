class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1
        

        def binarySearch(start,end,target):
            if start > end:
                return -1
            mid=(start+end)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                return binarySearch(start,mid-1,target)
            if nums[mid]<target:
                return binarySearch(mid+1,end,target)

        return binarySearch(start,end,target)
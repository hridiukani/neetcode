class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_list=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                diff=target-nums[i];
                if (diff==nums[j]):
                    num_list.append(i)
                    num_list.append(j)
                continue

        return num_list
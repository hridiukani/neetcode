class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        zeros = 0
        for n in nums:
            if n == 0:
                zeros += 1
            else:
                prod *= n

        if zeros > 1:
            return [0] * len(nums)

        res = []
        for n in nums:
            if zeros == 1:
                res.append(prod if n == 0 else 0)
            else:
                res.append(prod // n)
        return res
        
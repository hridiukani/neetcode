class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        for i in nums:
            res[i] += 1
        res_desc = sorted(res.items(), key=lambda item: item[1], reverse=True)
        return [item[0] for item in res_desc[:k]]
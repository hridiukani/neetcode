class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_d={}
        for i in s:
            count_d[i]=s.count(i)
        print(count_d)
        val=count_d.values()
        return max(val)+k
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_a=0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                max_a=max(max_a,((min(heights[j],heights[i]))*(j-i)))
        return max_a
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max=0
        w=0
        h=0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                w=j-i
                if heights[j]>heights[i]:
                    h=heights[i]
                else:
                    h=heights[j]
                area=w*h
                if area>=max:
                    max=area
        return max
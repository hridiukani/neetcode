class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=[]
        s=[0,-1,1]
        t=[1,-1,0]
        if s.sort() not in l:
            l.append(s)
            print(l)
        for i in l:
            print("i",i)
        print(l)
        
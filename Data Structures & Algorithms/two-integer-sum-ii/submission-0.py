class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res=[]
        for i in range(len(numbers)):
            two=target-numbers[i]
            for j in range(i+1,len(numbers)):
                if numbers[i]!=numbers[j] and numbers[j]==two:
                    res.append(numbers[i])
                    res.append(numbers[j])
                    break
        return res
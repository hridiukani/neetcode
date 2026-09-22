class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output=[]
        visited=[False]*len(strs)
        for i in range(len(strs)):
            temp_l=[]
            
            if visited[i]:
                continue
            
            temp_l.append(strs[i])
            visited[i]=True
            for j in range(i+1,len(strs)):
                if not visited[j] and sorted(strs[i])==sorted(strs[j]):
                    temp_l.append(strs[j])
                    visited[j]=True
            output.append(temp_l)
        return output



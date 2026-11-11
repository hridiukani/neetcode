class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        U: only uppercase alphabets, replacing any character at most k times
        P: 1) use a dict for storing frequency
            2) once iteration done, compare with k, update size accordingly

        """
        res=0
        seen=set(s)
        
        for c in seen:
            count=l=0
            for r in range(len(s)):
                if s[r]==c:
                    count+=1
                
                while (r-l+1)-count>k:
                    if s[l]==c:
                        count-=1
                    l+=1

                res=max(res,r-l+1)
        return res
        
            

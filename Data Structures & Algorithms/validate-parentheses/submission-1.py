class Solution:
    def isValid(self, s: str) -> bool:
        open_b={'(','{','['}
        close_b= {'}',']',')'}
        new=[]
        for i in s:
            if i in open_b:
                new.append(i)
            if i in close_b and new:
                if (i=='}' and new.pop()!='{') or (i==')' and new.pop()!='(') or (i==']' and new.pop()!='['):
                    return False
        return True

    
        
        
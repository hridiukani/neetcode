class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s=''
        for i in s:
            if i.isalpha():
                new_s+=i.lower()
        return (new_s==new_s[::-1])
        
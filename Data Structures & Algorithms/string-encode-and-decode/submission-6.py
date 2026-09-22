class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            print("empty")
            return ""
        print("ans=", " ".join(strs))
        return " ".join(strs)

    def decode(self, s: str) -> List[str]:
        if s=="":
            return []
        return s.split(" ")

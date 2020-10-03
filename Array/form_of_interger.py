class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        if not A:
            return K
        s = [str(i)for i in A]
        res = int("".join(s))
        val = res + K
        val = list(str(val))
        
        return val
            
        
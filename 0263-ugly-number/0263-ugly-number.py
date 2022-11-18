class Solution:
    def isUgly(self, n: int) -> bool:
        
        if n <= 0:
            return False
        
        return ((2*3*5) ** 32) % n == 0

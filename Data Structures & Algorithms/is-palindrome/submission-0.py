class Solution:
    def format(self, s: str) -> str:
        return "".join([c.lower() for c in s if c.isalnum()])

    def isPalindrome(self, s: str) -> bool:

        sClean = self.format(s)

        l = 0
        r = len(sClean) - 1


        while l < r:
            if sClean[l] != sClean[r]:
                return False
            l+=1
            r-=1
        
        return True
        
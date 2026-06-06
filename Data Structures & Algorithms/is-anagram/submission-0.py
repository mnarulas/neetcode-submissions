class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        sFreq = {}
        for c in s: 
            if c in sFreq:
                sFreq[c]+=1
            else:
                sFreq[c]=1
        
        tFreq = {}
        for c in t: 
            if c in tFreq:
                tFreq[c]+=1
            else:
                tFreq[c]=1
        
        sChars = sFreq.keys()
        tChars = tFreq.keys()

        if len(sChars) != len(tChars): 
            return False
        
        for c in sChars:
            if c not in tFreq:
                # mismatch!
                return False
            
            if tFreq[c] != sFreq[c]:
                return False
        
        return True



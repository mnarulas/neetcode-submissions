class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        reverseLookUp = set(nums)
        
        # get all nums that could be start of sequence 
        startingNums = [ n for n in nums if n-1 not in reverseLookUp]

        # of all sequences found, which is longest
        # this is O(n) given we only iterate on each num only once 
        longestSeries = 0
        for n in startingNums:
            consecutiveCounter = 0
            while n+consecutiveCounter in reverseLookUp:
                consecutiveCounter+=1
            longestSeries=max(longestSeries, consecutiveCounter)
        
        return longestSeries

        
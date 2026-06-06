class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contained = set()
        for n in nums:
            if n in contained: 
                return True
            else:
                contained.add(n)
        return False
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        num --> idx of num
        '''
        reverseLookup = {}
        
        for idx in range(len(nums)): 
            complement = target - nums[idx]
            if complement in reverseLookup: 
                return [reverseLookup[complement], idx]
            else: 
                reverseLookup[nums[idx]] = idx
            
        return [-1,-1]
        
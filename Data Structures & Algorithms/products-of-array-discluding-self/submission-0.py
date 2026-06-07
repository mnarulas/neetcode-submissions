class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        eg of nums: [1,2,3,4]
        prefixProduct is running product of all numbers before, including itself
        [1, 1*2, 1*2*3, 1*2*3*4]

        suffixProduct is running product of all numbers after, including itself
        [4*3*2*1, 4*3*2, 4*3, 4]

        so res can be calculated as product of all but itself 
           value at position i --> prefixProduct[i-1] X suffixProduct[i+1]
        '''
        prefixProduct = []
        suffixProduct = []
        res = []
        N = len(nums)

        prefixRunningProduct = 1
        for i in range(N):
            prefixRunningProduct *= nums[i]
            prefixProduct.append(prefixRunningProduct)
        
        suffixRunningProduct = 1
        for i in range(N-1, -1, -1):
            suffixRunningProduct *= nums[i]
            suffixProduct.insert(0,suffixRunningProduct)
        
        for i in range(N):
            prefix = 1
            if i > 0:
                prefix = prefixProduct[i-1]
            suffix = 1
            if i < N-1:
                suffix = suffixProduct[i+1]
            res.append(prefix*suffix)
        
        return res


        
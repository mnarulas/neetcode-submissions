class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        2ptr approach
        Since list is sorted, we will start with
        - one pointer on start of array (left)
        - one pointer on end of array (right)

        if sum is greater than target, 
           we need to reduce sum so we move right one to the left
        
        if sum is less than target, 
           we need to increase sum so we move left one to the right
          
        '''

        l = 0
        r = len(numbers) - 1

        while (l < r):
            ttl = numbers[l] + numbers[r]
            
            if ttl == target:
                return [l+1,r+1]
            elif ttl < target:
                # need to increase sum
                l+=1
            else:
                # ttl > target
                # need to decrease sum
                r-=1
        return []
        
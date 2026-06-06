class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        '''
        num --> frequency
        key.     value
        '''
        freq = {}
        for n in nums: 
            freq[n] = 1 + freq.get(n, 0)
        
        import heapq
        freqHeap = []
        for key in freq.keys():
            # max heap 
            heapq.heappush(freqHeap, (-freq[key], key))
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(freqHeap)[1])
        return res

        



        


        
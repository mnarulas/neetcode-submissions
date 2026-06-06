class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        alphabetically_sorted_annagram --> [word_1, word_2, ...]
        eg: "aht": ["hat", "tah"]
        '''
        sortedStrs = {}

        for w in strs:
            key = str(sorted(w))
            if key in sortedStrs:
                sortedStrs[key].append(w)
            else:
                sortedStrs[key] = [w]
        res = []
        for k in sortedStrs.keys():
            res.append(sortedStrs[k])
        
        return res

        
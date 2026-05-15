class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for i in nums:
            if i not in res:
                res[i] = 0
            res[i]+=1
        
        # print(res.items())
        a = sorted(res.items(),key= lambda x: x[1],reverse=True)[:k]
        # print(a)
        return([i[0] for i in a])
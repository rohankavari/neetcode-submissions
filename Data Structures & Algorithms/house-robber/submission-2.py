class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0],nums[1])
        d = []
        d.append(nums[0])
        d.append(max(nums[0],nums[1]))

        for i in range(2,len(nums)):
            r = max(d[i-1],nums[i] + d[i-2])

            d.append(r)
        
        return d[-1]
        
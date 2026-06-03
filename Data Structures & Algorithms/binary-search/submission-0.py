class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        mid = (l + r) //2
        while l <= mid:
            print(f"{nums[l]} {nums[mid]} {nums[r]}")
            if nums[mid] == target: return mid
            elif nums[mid]<target:
                l = mid + 1
            else:
                r = mid - 1
            mid = (l + r) // 2
        return -1
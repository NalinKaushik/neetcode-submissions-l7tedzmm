class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        end = n - 1
        minelem = float('inf')
        while(start<=end):
            mid = start + (end - start)//2
            minelem = min(minelem, nums[mid])
            if nums[mid] < nums[end]:
                end = mid - 1
            else:
                start = mid + 1
        return minelem

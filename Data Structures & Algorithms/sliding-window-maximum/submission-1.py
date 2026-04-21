class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        p1 = 0
        p2 = k-1
        maxnum = 0
        l1 = []
        length = 0  
        while(p2<n):
            curr = nums[p2]
            maxnum = max(nums[p1:p2+1])
            l1.append(maxnum)
            p1+=1
            p2+=1
        return l1
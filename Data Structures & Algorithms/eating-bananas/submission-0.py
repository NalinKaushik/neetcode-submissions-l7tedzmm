class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        end = max(piles)
        start = 1
        minrate = end
        h1 = 0
        while(start<=end):
            mid = start + (end - start)//2
            h1 = 0
            for i in piles:
                h1 += (i // mid)
                if i % mid > 0:
                    h1+=1
            if h1<=h:
                minrate = min(minrate, mid)
                end = mid - 1
            elif h1>h:
                start = mid + 1
        return minrate
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<=0:
            return 0
        length = 0
        max_length = 0
        setnums = set(nums)
        for num in setnums:
            if (num-1) not in setnums:
                length = 1
                while(num+1 in setnums):
                    num+=1
                    length+=1
                max_length = max(length,max_length) 
        return max_length
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        j=0
        for i in range(len(nums)):
            j = target - nums[i]
            if j in dic:
                return [dic[j],i]
            dic[nums[i]] = i
        
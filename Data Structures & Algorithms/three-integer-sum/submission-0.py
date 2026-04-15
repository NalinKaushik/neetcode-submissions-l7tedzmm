class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        i = 0
        j = n-2
        k = n-1
        list1 = []
        while(i<n-2):
            target = 0 - nums[i]
            j = i+1
            k = n-1
            while(j<k):
                add = nums[j] + nums[k]
                if add < target:
                    j+=1
                elif add > target:
                    k-=1
                else:
                    if [nums[i],nums[j],nums[k]] not in list1:
                        list1.append([nums[i],nums[j],nums[k]])
                    k-=1
            i+=1
        return list1



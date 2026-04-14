class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        list1 = []

        for i in nums:
            p*=i

        for j in range (len(nums)):

            if nums[j]==0:
                p2=1

                for k in range(len(nums)):
                    if k != j:
                        p2 *= nums[k]
                product = p2
            else:
                product = p//nums[j]

            list1.append(product)

        return list1

        # find solution for 0 by avoiding
        # the index of the 0 value
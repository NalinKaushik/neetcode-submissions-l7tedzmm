class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        dic2 = defaultdict(list)
        list1 = []
        amount = 0

        for i in nums:
            dic[i]+=1

        for key,value in dic.items():
            dic2[value].append(key)

        for key,value in sorted(dic2.items(), reverse = True):
            for m in value:
                amount+=1
                list1.append(m)
                if amount == k:
                    return list1

        
            
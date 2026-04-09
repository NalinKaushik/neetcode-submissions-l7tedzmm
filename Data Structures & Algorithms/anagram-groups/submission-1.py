class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            l1 = [0]*26
            for char in s:
                l1[ord(char) - ord('a')]+=1
            dic[tuple(l1)].append(s)

        return list(dic.values()) 




        
            
        

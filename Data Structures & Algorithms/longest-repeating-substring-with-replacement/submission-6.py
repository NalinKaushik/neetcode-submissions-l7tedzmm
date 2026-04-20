from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        dic = defaultdict(int)
        length = maxlength = 0
        p1 = i = m = 0
        while(i<n):
            curr = s[i]
            dic[curr]+=1
            m = max(m,dic[curr])
            remain_dist = abs((i+1 - p1) - m)
            if remain_dist > k:
                dic[s[p1]]-=1
                p1+=1
                
            else:
                length = i+1 - p1
                maxlength = max(maxlength, length) 
            i+=1

        return maxlength      

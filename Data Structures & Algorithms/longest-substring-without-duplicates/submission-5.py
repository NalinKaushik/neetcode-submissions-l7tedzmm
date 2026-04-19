class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if not n:return 0
        dic = {}
        p1 = maxlength = 0
        for i in range(n):

            if s[i] not in s[p1:i]:
                dic[s[i]] = i
               
            else:               
                p1 = dic[s[i]] + 1
                dic[s[i]] = i
                
            length = i-p1+1
            maxlength = max(maxlength, length)

        return maxlength
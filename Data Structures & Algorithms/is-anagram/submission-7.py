class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dic={}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in t:
            if i not in dic:
                return False
            dic[i]-=1
            if dic[i]<0:
                return False
        return True
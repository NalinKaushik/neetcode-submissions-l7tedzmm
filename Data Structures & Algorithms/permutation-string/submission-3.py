class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        s1 = sorted(s1)
        if n1 > n2:
            return False
        for i in range((n2-n1)+1):
            p2 = i+(n1-1)
            curr = s2[i]
            if curr in s1:
                if sorted(s2[i:p2+1]) == s1:
                    return True
        return False
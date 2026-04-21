class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        l1 = [0] * 26
        l2 = [0] * 26 
        for i in s1:
            l1[ord(i) - ord('a')]+=1

        p1 = 0
        p2 = 0
        while(p2<n2):
            curr = s2[p2]
            length = (p2 - p1) + 1
            l2[ord(curr) - ord('a')] += 1
            if length == n1:
                if l1 == l2:
                    return True
                else:
                    l2[ord(s2[p1]) - ord('a')] -= 1
                    p1+=1
            p2+=1
        return False 

           






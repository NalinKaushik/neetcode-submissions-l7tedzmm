class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        l1 = [0] * 58
        l2 = [0] * 58
        for i in t:
            l1[ord(i) - ord('A')] += 1
        nstring = ''
        p1 = 0
        p2 = 0
        need = len(set(t))
        have = 0
        minlength = float('inf')
        while(p2<n):
            curr = s[p2]
            if s[p2] in t:
                l2[ord(curr) - ord('A')] += 1
                if l2[ord(curr) - ord('A')] == l1[ord(curr) - ord('A')]:
                    have+=1
            while(have == need):
                length = (p2+1) - p1
                if minlength > length:
                    nstring = s[p1:p2+1]
                    minlength = length
                if s[p1] in t:
                    l2[ord(s[p1]) - ord('A')] -= 1
                    if l2[ord(s[p1]) - ord('A')] < l1[ord(s[p1]) - ord('A')]:
                        have -= 1
                p1+=1
            p2 += 1
        return nstring


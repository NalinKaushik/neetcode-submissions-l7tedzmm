class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1 = 0
        p2 = len(s)-1
        s = s.lower()

        while(p1<p2):
            val1 = s[p1]
            val2 = s[p2]
            if not val1.isalnum():
                p1+=1
                continue

            if not val2.isalnum():
                p2-=1
                continue
                
            if val1!=val2:
                return False
            p1+=1
            p2-=1
        return True
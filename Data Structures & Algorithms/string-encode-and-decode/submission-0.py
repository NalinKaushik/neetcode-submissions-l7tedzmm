from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        s = ''
        for word in strs:
            s += str(len(word)) + '#' + word
        return s

    def decode(self, s: str) -> List[str]:
        list1 = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
                
            length = int(s[i:j])
            
            word_start = j + 1
            word_end = word_start + length
            
            list1.append(s[word_start:word_end])
            
            i = word_end
            
        return list1
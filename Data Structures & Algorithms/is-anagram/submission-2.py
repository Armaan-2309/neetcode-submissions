class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        tag = [0] * 26
        
        for i in range(len(s)):
            tag[ord(s[i]) - ord('a')] +=1
            tag[ord(t[i]) - ord('a')] -=1
        
        return all(n == 0 for n in tag)
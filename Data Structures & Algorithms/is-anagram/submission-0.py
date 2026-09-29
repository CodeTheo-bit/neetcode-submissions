class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {}
        hp = {}
        for i in s:
            hm[i] = hm.get(i,0)+1
        
        for i in t:
            hp[i] = hp.get(i,0)+1
        
        if sorted(s)==sorted(t):
            return True
        else:
            return False
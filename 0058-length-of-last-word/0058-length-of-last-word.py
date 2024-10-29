class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list= s.split()
        if len(list)==0:
            return 0
        return len(list[-1])
        
        
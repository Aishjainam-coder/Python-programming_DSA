class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""

        length= max (len(word1), len(word2))   # dekh ese length nikalte 
        for i in range(length):
            if i < len(word1):
                merged += word1[i]   # if k andar if bhi lga sakte 
            if i < len(word2): 
                merged += word2[i]

        return merged        
            
             

    

        
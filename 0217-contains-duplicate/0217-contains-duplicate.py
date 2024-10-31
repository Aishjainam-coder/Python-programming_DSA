class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n= set()
        for i in nums:
            if i in n :
                return True  # If yes, return True (duplicate found)
            n.add(i)  # If not, add the number to the set
            
        return False  
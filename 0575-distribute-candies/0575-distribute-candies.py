class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        max= n//2
        unique= set(candyType)
        return min(len(unique), max)



        
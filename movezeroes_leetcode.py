from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        prev=0

        for i in range(0,len(nums)):
            if nums[i]!=0:
                hold=nums[prev]
                nums[prev]=nums[i]
                nums[i]=hold
                prev=prev+1
                
                
sol = Solution()
nums = [0, 1, 0, 3, 12]
sol.moveZeroes(nums)
print(nums)  # Out
        

        
            

nums = [0, 1, 0, 3, 12]

prev = 0

for i in range(0, len(nums)):
    if nums[i] != 0:
        hold = nums[prev]
        nums[prev] = nums[i]
        nums[i] = hold
        prev += 1

print(nums)  # Output: [1, 3, 12, 0, 0]    
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-1]*nums[-2]* nums[-3]   , nums[0]*nums[1]* nums[-1])
     #iska mtlb ki maximum dhundho mtlb dono me se  comma k phle normal 
     #aur comma k baad jo aur ho sakta wo i mean smallest smallest largest 
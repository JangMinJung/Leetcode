class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums=sorted(nums)
        nums=nums[::-1]
        answer=(nums[0]-1)*(nums[1]-1)
        return answer
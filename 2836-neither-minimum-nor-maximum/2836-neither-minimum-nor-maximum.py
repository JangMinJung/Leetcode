class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums=sorted(nums)
        if len(nums)==2 or len(nums)==1:
            answer=-1
        else:
            answer=nums[1]
        return answer    

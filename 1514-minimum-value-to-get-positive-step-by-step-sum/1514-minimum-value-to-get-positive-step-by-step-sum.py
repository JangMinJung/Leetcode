class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        if nums[0] <=0:
            answer= abs(nums[0])+1
        else:
            answer=1
        j=0    
        for num in nums:
            j+=num    
            if answer+j <1:
                answer+=abs(j+answer)+1
        return answer 
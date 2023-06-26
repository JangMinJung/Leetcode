class Solution:
    def averageValue(self, nums: List[int]) -> int:
        j=0
        sum_all=0
        answer=0
        for i in nums:
            if i%6==0 :
                j+=1
                sum_all+=i
                print(sum_all)
                answer=int((sum_all)/j)
            
        return answer        
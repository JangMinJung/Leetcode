class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sub_num=[]
        if len(nums)>=3:
            for i in range(len(nums)-1):
                sum_num=nums[i]+nums[i+1]
                sub_num.append(sum_num)
                set_num=set(sub_num)
                if len(set_num)!=len(sub_num):
                    answer= True
                    break
                else:
                    answer= False
        else : 
            answer= False            
        return answer        
        



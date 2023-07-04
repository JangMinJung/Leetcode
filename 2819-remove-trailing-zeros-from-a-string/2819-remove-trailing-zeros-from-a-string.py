class Solution:
    def removeTrailingZeros(self, num) :
        for i in range(len(num)):
            num=int(num)
            if num%10==0:
                num=num//10
                num=int(num)
                num=str(num)
            else:
                num=num
        return str(num)  
       

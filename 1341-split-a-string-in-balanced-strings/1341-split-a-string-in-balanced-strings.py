class Solution:
    def balancedStringSplit(self, s: str) -> int:
        s_list=[]
        for i in s:
            if i=="R":
                i=1
                s_list.append(i)
            else:
                i=-1
                s_list.append(i)
        print(s_list)      
        j=0
        k=0
        for i in s_list:
            j+=i
            if j==0:
                k+=1  
        return k
               



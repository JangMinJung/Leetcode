class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        s_list=list(s)
        B=[]
        for i in range(len(s_list)):
            B.append(ord(s_list[i])-64)
        print(B)    
        C=[]
        D=[]
        for j in range(len(B)-1):
            if B[j+1]==B[j]+1:
                C.extend(B[j:j+2])
                print(C)
                E=set(C)
                D.append(len(list(E)))
            else:
                C=[]
        if not D:
            answer=1
        else:
            answer=max(D)
        return answer


            

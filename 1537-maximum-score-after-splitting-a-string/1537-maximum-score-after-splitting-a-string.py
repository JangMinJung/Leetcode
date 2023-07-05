class Solution:
    def maxScore(self, s: str) -> int:
        max_list=[]
      
        for i in range(len(list(s))-1):
            A=Counter(s[:i+1])
            B=Counter(s[i+1:])
            print(A)
            C=A["0"]+B["1"]
            max_list.append(C)
            print(max_list)
            answer=max(max_list)

        D=Counter(s[:-1])
        E=Counter(s[-1])
        F=D["0"]+E["1"]
        if answer<F:
            answer=F
        return answer    
class Solution:
    def isFascinating(self, n: int) -> bool:
        n_2=n*2
        n_3=n*3
        n=str(n)
        n_2=str(n_2)
        n_3=str(n_3)
        total_n=n+n_2+n_3
        total_n=sorted(total_n)

        j=1
        for i in range(len(total_n)):
            if int(total_n[i])==j:
                answer= True

                j+=1
                
            else:    
                answer=False
                break



        return answer                 
                        

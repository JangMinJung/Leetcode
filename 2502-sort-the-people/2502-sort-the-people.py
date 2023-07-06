class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_sor=sorted(heights, reverse=True)
       
        A={}
        for i  in range(len(heights)):
            A={x:y for x,y in zip(heights,names)}
           
        B=[]    
        for j in height_sor:
            k=A[j]
            B.append(k)
        return B    
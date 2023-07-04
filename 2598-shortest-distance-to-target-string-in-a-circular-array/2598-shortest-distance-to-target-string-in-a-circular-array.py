class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        k=startIndex
        words_two=words*2
        print(words_two)
        count=[]
        if not target in words:
            answer=-1
        
        else:

            for i in range(0,len(words_two)-k):
                if words_two[k+i]==target:
                    count.append(i)
                    print(count)
            for i in range(0,len(words)+k+1):        
                if words_two[k+len(words)-i]==target:
                    count.append(i)
                    print(count)
                    count=[abs(i) for i in count]
            answer=min(count)        
         
        return answer


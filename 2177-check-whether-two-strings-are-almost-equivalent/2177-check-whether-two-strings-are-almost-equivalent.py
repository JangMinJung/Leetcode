class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        from collections import Counter
        word1_dict=Counter(word1)
        word2_dict=Counter(word2)
        for ele in word1_dict:
            if abs(word1_dict[ele]-word2_dict[ele])>3:
                A= 0
                break
            else: 
                A= 1
        for elel in word2_dict:
            if abs(word1_dict[elel]-word2_dict[elel])>3:
                B=0
                break 
            else: 
                B= 1    
            print(B)    
        if A+B==2:
            return True
        else:
            return False        

        

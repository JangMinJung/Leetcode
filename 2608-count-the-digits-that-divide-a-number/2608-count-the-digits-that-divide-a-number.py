class Solution:
    def countDigits(self, num: int) -> int:
        num_str=str(num)
        print(num)
        j=0
        for i in num_str:
            if num%int(i)==0:
                j+=1
        return j        
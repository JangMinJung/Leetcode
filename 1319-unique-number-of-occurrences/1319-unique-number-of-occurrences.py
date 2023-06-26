class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        arr_dict=Counter(arr)
        arr_list=[]
        for i,j in arr_dict.items():
            arr_list.append(arr_dict[i]) 
        if len(arr_list)==len(set(arr_list)):
            return True
        else: 
            return False        
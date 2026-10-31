class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if not strs:
            return [""]
        word_dict = {}

        for s in strs:
            tuple_list = []
            for char in s:
                tuple_list.append((char, 1))
            tuple_list.sort()
            
            key = tuple(tuple_list)
            if key not in word_dict:
                word_dict[key] = []
            word_dict[key].append(s)
      
        return_list = []
        for key, value in word_dict.items():
            return_list.append(value)
        
        return return_list

       

        
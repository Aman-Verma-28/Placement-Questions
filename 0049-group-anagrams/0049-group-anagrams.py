class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        
        for string in strs:
            list_val = [0 for i in range(26)]
            for cur in string:
                list_val[ord(cur)-ord('a')]+=1
            
            tuple_val = tuple(list_val)
            if tuple_val in hashmap:
                hashmap[tuple_val].append(string)
            else:
                hashmap[tuple_val]=[string]
        
        return hashmap.values()
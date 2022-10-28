class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        
        for string in strs:
            sorted_val = "".join(sorted(string))
            if sorted_val in hashmap:
                hashmap[sorted_val].append(string)
            else:
                hashmap[sorted_val]=[string]
                
        return hashmap.values()
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}
        for val in arr:
            if val in hashmap:
                hashmap[val] += 1
            else:
                hashmap[val] = 1
        
        return len(hashmap) == len(set(hashmap.values()))
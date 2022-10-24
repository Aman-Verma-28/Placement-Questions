class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        
        def recursive(index, arr, maxLength, curLength, visited):
            if index<0:
                maxLength[0] = max(maxLength[0], curLength[0])
                return
            vis_new = [i for i in visited]
            cur = [curLength[0]]
            string = arr[index]
            if len(string) == len(set(string)):
                for char in string:
                    if visited[ord(char)-ord('a')]>0:
                        break

                else:
                    for char in string:
                        visited[ord(char)-ord('a')]+=1
                    curLength[0]+=len(string)
                    # maxLength[0] = max(maxLength[0], curLength[0])
                    recursive(index-1, arr, maxLength, curLength, visited)
                
                        
                
            
            
            # not take
            recursive(index-1, arr, maxLength, cur, vis_new)
            
            
            
        maxLength = [0]
        curLength = [0]
        index = len(arr)-1
        visited = [0 for i in range(26)]
        
        recursive(index, arr, maxLength, curLength, visited)
        
        return maxLength[0]
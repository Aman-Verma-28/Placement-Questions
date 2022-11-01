#User function Template for python3

class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        left = 0
        top = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
    
        traversalArray = []
    
        while top <= bottom or left <= right:
            pointer = left
            while pointer <= right:
                traversalArray.append(matrix[top][pointer])
                pointer += 1
            top += 1
            
            if top > bottom or right < left:
                break
            
            pointer = top
            while pointer <= bottom:
                traversalArray.append(matrix[pointer][right])
                pointer += 1
            right -= 1
    
            if top > bottom or right < left:
                break
    
            pointer = right
            while pointer >= left:
                traversalArray.append(matrix[bottom][pointer])
                pointer -= 1
            bottom -= 1
            
            if top > bottom or right < left:
                break
    
            pointer = bottom
            while pointer >= top:
                traversalArray.append(matrix[pointer][left])
                pointer -= 1
            left += 1
    
        return traversalArray
            
            
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        
        def knows(first, second):
            return bool(M[first][second])
            
        
        stack = [i for i in range(n)]
        
        while len(stack)>1:
            first = stack.pop()
            second = stack.pop()
            
            if knows(first, second):
                stack.append(second)
            else:
                stack.append(first)
        
        candidate = stack.pop()
        
        for val in M[candidate]:
            if val==1:
                return -1
        
        for index in range(n):
            if index!=candidate:
                if M[index][candidate]==0:
                    return -1
        
        return candidate



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends
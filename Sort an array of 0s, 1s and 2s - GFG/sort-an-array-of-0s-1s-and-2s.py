#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        zero = 0
        one = 0
        two = n-1
        while one<=two:
            if arr[one]==0:
                arr[zero], arr[one] = arr[one], arr[zero]
                zero+=1
                one+=1
            elif arr[one]==2:
                arr[one], arr[two] = arr[two], arr[one]
                two-=1
            else:
                one+=1
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends
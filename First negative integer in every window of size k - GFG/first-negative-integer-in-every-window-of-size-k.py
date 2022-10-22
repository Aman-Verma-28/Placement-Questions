#User function Template for python3
from collections import  deque
def printFirstNegativeInteger( a, n, k):
    # code here
    queue = deque()
    count=0
    for i in range(k-1):
        if a[i]<0:
            queue.append(i)
            count+=1
    ans = []
    start=0
    for i in range(k-1, n):
        if a[i]<0:
            queue.append(i)
            count+=1
        if count==0:
            ans.append(0)
        else:
            ans.append(a[queue[0]])
            if queue[0]==start:
                queue.popleft()
                count-=1
        start+=1

        # print(queue, i)
    return ans
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends
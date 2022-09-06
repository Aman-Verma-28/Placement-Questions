def fun(arr,n):
    #write your code here
    zero = 0
    one = 0
    two = n - 1
    while one < two:
        if arr[one] == 1:
            one += 1
        elif arr[one] == 0:
            arr[zero], arr[one] = arr[one], arr[zero]
            zero += 1
            one += 1
        else:
            arr[one], arr[two] = arr[two], arr[one]
            two -= 1


composition=[2,3,1,2]
stock=[3,6,2,2]
cost=[2,2,5,9]
budget=10


print(fun([
0, 1 ,2 ,2 ,1 ,0],6))
# fun(composition, stock, cost, budget)
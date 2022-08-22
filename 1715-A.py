# import math
from collections import Counter, deque, defaultdict
from math import *

from bisect import bisect_right

mod = 1000000007


# from functools import reduce
# from itertools import permutations
# import queue

def solve():
    n,m = list(map(int,input().split()))
    if n==1 and m==1:
        print(0)
        return
    if n==1:
        print(m)
        return
    if m==1:
        print(n)
        return
    ans=n+m-2
    ans+=min(n,m)
    print(ans)
t = int(input())
# t = 1
for num in range(t):
    # print("Case #{}: ".format(num + 1), end="")
    solve()


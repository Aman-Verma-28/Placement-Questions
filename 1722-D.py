from math import *
from collections import Counter





def solve():
	n = int(input())
	s = input()
	left = []
	right = []
	l=0
	r=0
	for i in range(n//2-1,-1,-1):
		if s[i]=='L':
			l+=1
			left.append([n-1-i, i])
	for i in range(n//2, n):
		if s[i]=='R':
			r+=1
			right.append([i, n-1-i])
	ans = []
	curScore=0
	for i in range(n):
		if s[i]=='L':
			curScore+=i
		else:
			curScore+=n-1-i
	for i in range(n):
		if r==0 and l==0:
			ans.append(curScore)
		elif r==0:
			x=left.pop()
			curScore+=x[0]-x[1]
			ans.append(curScore)
			l-=1
		elif l==0:
			x=right.pop()
			curScore+=x[0]-x[1]
			ans.append(curScore)
			r-=1
		else:
			if right[-1][0]>=left[-1][0]:
				x=right.pop()
				curScore+=x[0]-x[1]
				r-=1
			else:
				x=left.pop()
				curScore+=x[0]-x[1]
				l-=1
			ans.append(curScore)
	print(*ans)

for _ in range(int(input())):
	solve()
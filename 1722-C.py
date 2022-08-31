from math import *
from collections import Counter





def solve():
	n = int(input())
	p1 = set(input().split())
	p2 = set(input().split())
	p3 = set(input().split())
	s1 = 0
	s2 = 0
	s3 = 0
	cnt = 0
	for i in p1:
		t2 = i in p2
		t3 = i in p3
		if t2 and t3:
			cnt += 1
			continue
		elif t2:
			s1+=1
			s2+=1
		elif t3:
			s1+=1
			s3+=1
			cnt+=1
		else:
			s1+=3
	for i in p2:
		t1 = i in p1
		t3 = i in p3
		if t1 and t3:
			continue
		elif t3:
			cnt+=1
			s2+=1
			s3+=1
		elif t1:
			continue
		else:
			s2+=3
	for i in p3:
		t1 = i in p1
		t2 = i in p2
		if t1 and t2:
			continue
		elif t1:
			continue
		elif t2:
			continue
		else:
			s3+=3
	# s3+=(n-cnt)*3
	print(s1,s2,s3)

for _ in range(int(input())):
	solve()
#coding=utf-8
import time
def fib_rec(n):
	if n < 1:
		print 'input error'
		return -1
	if n == 1 or n==2:
		return 1
	else:
		return fib_rec(n-1) + fib_rec(n-2)
def fib_ite(n):
	n1 = 1
	n2 = 1
	n3 = 1
	if n<1:
		print 'input error'
		return -1
	while (n-2) > 0:
		n3 = n2 + n1
		n1 = n2
		n2 = n3
		n -= 1
	return n3
#用迭代计算
time1 = time.time()
print fib_ite(35)
print time.time() - time1
#用递归计算
time1 = time.time()
print fib_rec(35)
print time.time() - time1
'''输出结果：递归所用时间大得多
9227465
1.59740447998e-05
9227465
2.28218698502
[Finished in 2.3s]
'''

	
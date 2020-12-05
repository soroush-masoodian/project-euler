import math as m
import sys

sys.setrecursionlimit(100000)


def triangle_num(n):
	if n <= 1:
		return n
	else:
		return n + triangle_num(n-1)


def num_divisors(num):
	divisors = 0
	i = 1
	while i <= m.sqrt(num):
		if num % i == 0:
			if num // i == i:
				divisors += 1
			else:
				divisors += 2
		i += 1

	return divisors


def main():
	i = 1
	nd = 0
	tn = 0
	while nd <= 500:
		tn = triangle_num(i)
		nd = num_divisors(tn)
		i += 1

	print(tn, ":", nd)

main()

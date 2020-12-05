def collatz(n):
	if n % 2 == 0:
		return n // 2
	else:
		return 3*n + 1


def sequence(n):
	chain = 1
	while n != 1:
		n = collatz(n)
		chain += 1
	
	return chain


def main():
	longest = 0
	number = 0
	for i in range(1, 1000000):
		if sequence(i) > longest:
			longest = sequence(i)
			number = i
	
	print(longest, ":", number)


main()


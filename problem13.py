f = open('problem13-numbers.txt', 'r')
numbers = []
for line in f:
	numbers.append(int(line))

s = sum(numbers)
print(s)

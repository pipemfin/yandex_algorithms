input = open('input.txt', 'r')
output = open('output.txt', 'w')
numbers = []
for line in input:
	numbers.append(int(line))
input.close()
if (numbers[0] == 0):
	if (numbers[1] > 0):
		output.write("MANY SOLUTIONS")
	else (numbers[1] < 0):
		output.write("NO SOLUTIONS")
output.close()
input = open('input.txt', 'r')
output = open('output.txt', 'w')
numbers = []
for line in input:
	numbers.append(line.removesuffix('\n'))
input.close()
for i in range(len(numbers)):
	numbers[i] = numbers[i].replace("-", "").replace("(", "").replace(")", "").strip("+")
	if (len(numbers[i]) == 11):
		numbers[i] = numbers[i][1:]
	if (len(numbers[i]) == 7):
		numbers[i] = "495" + numbers[i]
for number in numbers[1:]:
	if (number == numbers[0]):
		output.write("YES\n")
	else:
		output.write("NO\n")
output.close()
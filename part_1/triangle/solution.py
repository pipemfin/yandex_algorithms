input = open('input.txt', 'r')
output = open('output.txt', 'w')
sides = []
for i in range(3):
	sides.append(int(input.readline()))
input.close()
if ((sides[0] + sides[1] > sides[2]) and (sides[0] + sides[2] > sides[1]) and (sides[1] + sides[2] > sides[0])):
	output.write("YES")
else:
	output.write("NO")
output.close()
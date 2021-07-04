input = open('input.txt', 'r')
output = open('output.txt', 'w')
params = []
for line in input:
	temp = line.split()
	for obj in temp:
		params.append(obj)
input.close()
if (params[2] == 'freeze'):
	output.write(str(min(int(params[0]), int(params[1]))))
elif (params[2] == 'heat'):
	output.write(str(max(int(params[0]), int(params[1]))))
elif (params[2] == 'auto'):
	output.write(params[1])
else:
	output.write(params[0])
output.close()
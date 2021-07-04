input = open('input.txt', 'r')
output = open('output.txt', 'w')
params = input.readline().split(' ')
input.close()
first_notebook = [int(params[0]), int(params[1])]
second_notebook = [int(params[2]), int(params[3])]
answers = {}
solution = 0
min_area = float('inf')
for a in range(2):
    for b in range(2):
        longest_side = max(first_notebook[1 - a], second_notebook[1 - b])
        area = (first_notebook[a] + second_notebook[b]) * longest_side
        answers[solution] = [area, (str((first_notebook[a] + second_notebook[b])) + ' ' + str(longest_side))]
        solution += 1
        min_area = min_area if min_area <= area else area
for key, value in answers.items():
    if (value[0] == min_area):
        output.write(value[1])
        break
output.close()
input = open('input.txt', 'r')
output = open('output.txt', 'w')
params = input.readline().split(' ')
input.close()
n, k, m = int(params[0]), int(params[1]), int(params[2])
remainder, blanks, details = 0, 0, 0
if (k <= n and m <= k):
    while (n >= k):
        blanks = n // k
        remainder = n % k
        details += k // m * blanks
        remainder += k % m * blanks
        n = remainder
output.write(str(details))
output.close()
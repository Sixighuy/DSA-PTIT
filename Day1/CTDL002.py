import itertools
line1 = input().split()
n = int(line1[0])
k = int(line1[1])
line2 = input().split()
a = []
for x in line2:
    a.append(int(x))
count = 0    
for bit in itertools.product([0,1], repeat = n):
    sum = 0
    result = []
    for i in range(n):
        if bit[i] == 1:
            sum = sum + a[i]
            result.append(a[i])
    if sum == k:
        print(*result)
        count += 1
print(count)
sum = []
sum.append(0)
sum.append(1)
sum.append(1)

for i in range(1,10):
    sum.append(sum[i] + sum[i+1])
    print(str(i) + ": " + str(sum[i]))

print(sum)


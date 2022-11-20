out = ""
for n in range(100):
    sum = 0
    for i in range(n):
        sum = sum + n/(n-i)
    print(str(n) + "," + str(sum))

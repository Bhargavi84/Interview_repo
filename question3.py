
N = input("Enter the number: ")

count = 0
for i in range(int(N)+1):
    if i == 0:
        count = 0
    if i >= 1 and i <= 99:
        j = i//10
        if j == 1:
            count+=1
        z = i%10
        if z == 1:
            count+=1
    if i == 100:
        count+=1

print(count)

print("Sum of n numbers")
print("------------------")

SN = int(input("Enter the starting number: "))
EN = int(input("Enter the ending number: "))

print("Result")
print("--------------------------")
print("Series")

count = 0
sum = 0

for i in range(SN, EN + 1):
    if (i % 5 == 0) and (i % 3 == 0):
        print("+", i, end=" ")
        sum += i
        count += 1

print("Sum value:", sum)
print("Count value:", count)


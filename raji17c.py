print("Sum of n numbers")
print("--------------------")

SN = int(input("Enter the starting number: "))
EN = int(input("Enter the ending number: "))
D = int(input("Enter the difference: "))

print("Result")
print("Series:")

sum = 0
count = 0

for i in range(SN, EN + 1, D):
    print("+", i, end=" ")
    sum += i
    count += 1

print("Sum value:", sum)
print("Count value:", count)
      

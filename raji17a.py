print("Sum of n number")
print("-----------------")

n=int(input("Enter the number:"))

sum=0
print("Result")

for i in range(1, n + 1):
    print("+", i, end=" ")
    sum+=i
    
print("sum of first","number is:",sum)
    

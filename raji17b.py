print("Sum of n number")
print("-----------------")

m1=int(input("Enter the starting number:"))
m2=int(input("Enter The Ending number:"))
sum=0
print("Result")

for i in range(m1, m2+1):
    print("+", i, end=" ")
    sum+=i
    
print("sum of first","number is:",sum)
    

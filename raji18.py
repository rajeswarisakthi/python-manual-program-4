print("Fibonacci series")
print("------------------")
n=int(input("Enter the number:"))
print("Fibonacci series")
a=1
b=1
for i in range(n+1):
    c=a+b
    print(c, end=" ")
    a= b
    b= c

print("Reverse number")
print("-----------------")
n = int(input("Enter the number:"))
print("Result")
print("Reverse number:")

reverse = 0

while n > 0:
    r = n % 10        
    reverse = reverse * 10 + r  
    n = n // 10       

print(reverse)


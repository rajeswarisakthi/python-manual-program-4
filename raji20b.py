print("Prime Number Checking")
print("-----------------------")

sn = int(input("Enter the starting number: "))
en = int(input("Enter the ending number: "))
print("RESULT")

for n in range(sn, en + 1):
    if n <= 1:
        print(n, "is not a prime")
        continue

    count = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            count += 1
            break

    if count == 0:
        print(n, "is a prime")
    else:
        print(n, "is not a prime")

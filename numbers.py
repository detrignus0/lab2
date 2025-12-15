print("Enter 4 numbers:")

n1 = float(input("Number 1: "))
n2 = float(input("Number 2: "))
n3 = float(input("Number 3: "))
n4 = float(input("Number 4: "))

sum1 = n1 + n2
sum2 = n3 + n4

if sum2 != 0:
    result = sum1 / sum2

    print(f"Result: {result:.2f}")
else:
    print("Division by zero is not allowed.")
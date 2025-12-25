x = int(input("Enter the base: "))
n = int(input("Enter the number of terms: "))

for i in range(1, n + 1):
    term = x ** i
    print(term, end=" ")
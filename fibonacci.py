num = int(input("Enter number of terms :"))

n1, n2 = 0, 1
count = 0

if num < 0:
    print("Please enter a positive integer")
elif num == 1:
    print("Fibonacci series upto", num, "is :")
    print(n1)
else:
    print("Fibonacci sequence :")
    while count < num:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

i = int(input("enter a number: "))
j = 2
while j <= (i / j):
    if not (i % j):
        print("not a prime number ")
        break
    j = j + 1
if j > i / j :
    print("prime number")

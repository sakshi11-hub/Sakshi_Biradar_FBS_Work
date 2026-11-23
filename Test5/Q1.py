D = [2000, 500, 200, 100, 50, 20, 10, 5]

amount = int(input("Enter amount: "))

for i in D:
    count = amount // i
    if count > 0:
        print(i, ":", count)
        amount = amount % i
## n = (input("Enter an Integer: "))
## for x in reversed(n):
##    print(x)

total = 0
print("Enter values, 0 to quit: ")
n = 1
while n != 0:
    n = int(input())
    if n != 0:
        total = total + n
print("Sum: ", total)

        


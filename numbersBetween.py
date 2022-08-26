num1 = int(input('Please input the first test number: '))
num2 = int(input('Please input the second test number: '))

if num2 > num1:
    for x in range(num1,num2):
        if x%7 == 0 and x%5 != 0:
            print(x)
else:
    for x in range(num2,num1):
        if x%7 == 0 and x%5 != 0:
            print(x)


    
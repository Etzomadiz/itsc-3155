time1 = int(input("First time: "))
suffix1 = input("suffix: ")
time2 = int(input("Second time: "))
suffix2 = input("suffix: ")

if suffix1 == suffix2 :
    if (time1 < time2):
        print("Before")
    else: 
        if time1 > time2:
            print("After")
        else:
            print("Same")
else:
    if suffix1 == "am":
        print("Before")
    else:
        print("After")

    
        
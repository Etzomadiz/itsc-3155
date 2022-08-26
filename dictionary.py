dictionary1 = {'a': 100,'b': 200,'c': 300}
dictionary2 = {'a': 300,'b': 200, 'd': 400}

dictionary3 = dict(dictionary1)
dictionary3.update(dictionary2)

for i, x in dictionary1.items():
    for j, y in dictionary2.items():
        if i == j:
            dictionary3[i]=(x+y)

print(dictionary3)





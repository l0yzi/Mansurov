import random
a = random.randint(22, 100)
print(a)

digits = [int(d) for d in str(a)]
for item in digits:
    print(type(item))
print(digits)




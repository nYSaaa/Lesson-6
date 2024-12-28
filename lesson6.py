import random

name = input("Enter your name")
print(name)

nlist = []

for x in name:
    nlist.append(x)
    print(x)

print(nlist)

list = [1,2,3,4,5,6,7,8,9]
sym = ["!" , "@" , "#" , "&" , "*"]

a = random.choice(nlist)
b = random.choice(nlist)
c = random.choice(list)
d = random.choice(list)
e = random.choice(sym)

print("Password : {}{}{}{}{}".format(b , e , d , c , a))

import random 

veg = ["Carrots " , "Spinach " , "Cucumber " , "Broccoli "]
fruits = ["Orange " , "Mango " , "Kiwi " , "Grapes " , "Watermelon " , "Apple "]
bread = ["Sourdough " , "Rye " , "Flatbread " , "Ciabatta "]

a = random.choice(veg)
b = random.choice(veg)
x = random.choice(fruits)
y = random.choice(bread)

print("Your meal today is : {}{}{}and {}".format(b , x , a , y))

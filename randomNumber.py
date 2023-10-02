import random
import my_modules

random_integer = random.randint(1,10) #return random integer number
random_range = random.randrange(1,10)
random_float = random.random() # default functionality provide random number between 0.0 to 1.0
print(float(random_integer))
print(random_range)
print(my_modules.pi)
print(random_float)
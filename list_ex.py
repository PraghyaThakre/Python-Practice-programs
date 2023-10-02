import random


names = input("enter the name of friends in , separeted form:")
names_list = names.split(",")
print(names_list)

name = random.choice(names_list)
print(f"{name} is goin to pay bill")


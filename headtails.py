import random

head = 1
tail = 0

head_or_tail = random.randint(0,1)
print(head_or_tail)
if(head_or_tail==0):
    print("tail")
else:
    print("head")    
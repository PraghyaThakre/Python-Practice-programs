import random
scisor = '''  ____
  / __ \
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/
'''

paper = ''' _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|            '''


rock = '''                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
                     
                     '''


rock_paper_scisor = [scisor,rock,paper]
user_input = input("enter the value either rock, scisor,paper: ")
PC_input = random.choice(rock_paper_scisor)
print(user_input)
print(f"PC Choice   {PC_input}")
if(user_input == 'rock' and PC_input == scisor):
    print("you win")
elif(user_input == 'scisor' and PC_input == paper):
    print("you win")
elif(user_input == 'paper' and PC_input == rock):
    print("you win")
else:
    print("you loss")            
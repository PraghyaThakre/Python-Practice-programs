import random
word_list = ['ardvark', 'baboon', 'camel']
display = []

choosen_word = random.choice(word_list)
print(choosen_word)

for i in choosen_word:
    display.append('_')

print(display)    

# guess = input("Guess the letter: ").lower()

end_of_game = False
while not end_of_game: 
    guess = input("Guess the letter: ").lower()
    for i in range(len(choosen_word)):
        letter = choosen_word[i]
        if letter == guess:
            display[i] = letter
    print(display)        
    if '_' not in display:
        end_of_game = True
        print("you win")    

          



# for i in choosen_word:
#     if guess == i:
#         print("Right")
#     else:
#         print("Wrong")    
    

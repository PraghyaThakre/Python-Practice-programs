def loveCalculator():
    her_name_old = input("enter her name: ")
    his_name_old = input("enter his name: ")
    her_name = her_name_old.lower()
    print(her_name)
    his_name = his_name_old.lower()
    first_word = "true".lower()
    second_word = "love".lower()
    first_digit=0
    second_digit=0
    first_digit += (her_name.count(first_word[0])+his_name.count(first_word[0]))
    first_digit += (her_name.count(first_word[1])+his_name.count(first_word[1]))
    first_digit += (her_name.count(first_word[2])+his_name.count(first_word[2]))
    first_digit += (her_name.count(first_word[3])+his_name.count(first_word[3]))
    second_digit += (his_name.count(second_word[0])+her_name.count(second_word[0]))
    second_digit += (his_name.count(second_word[1])+her_name.count(second_word[1]))
    second_digit += (his_name.count(second_word[2])+her_name.count(second_word[2]))
    second_digit += (his_name.count(second_word[3])+her_name.count(second_word[3]))
    love_Score_old = str(first_digit)+str(second_digit)
    love_Score = int(love_Score_old)
    if(love_Score>90):
       print(f"Your score is {love_Score}, you go together like coke and mentos.")
    elif(40<love_Score<50):
        print(f"Your score is {love_Score}, you are alright together.") 
    else:
        print(f"Your score is {love_Score}.")      


loveCalculator()    
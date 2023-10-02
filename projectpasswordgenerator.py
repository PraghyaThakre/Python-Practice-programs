import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
           , 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','x','Y','Z']
symbols = ['!','@','#','$','%','&','+','*']
digit = ['0','1','2','3','4','5','6','7','8','9']

print("Welcome to the password generator")
nr_letters = int(input("how many number of chracter pwd contain: "))
nr_symbols = int(input("provide the number of symbols include in pwd: "))
nr_digit = int(input("provide number of digit in pwd: "))

new_letters = ''
new_symbols = ''
new_digit = ''
for l in range(0, nr_letters+1):
    new_letters +=random.choice(letters)
for s in range(0,nr_symbols+1):
    new_symbols += random.choice(symbols)
for d in range(0,nr_digit+1):
    new_digit += random.choice(digit)

add_pwd = new_letters+new_digit+new_symbols
# add_pwd = add_pwd.split()
print(add_pwd)

##########################hard method for shuffling

password_list = []
for l in range(0, nr_letters+1):
    password_list +=random.choice(letters)
for s in range(0,nr_symbols+1):
    password_list += random.choice(symbols)
for d in range(0,nr_digit+1):
    password_list += random.choice(digit)


# print(password_list)

final_pwd = ''
random.shuffle(password_list)
# print(password_list)
for p in range(0,len(password_list)):
         final_pwd += password_list[p]

print(final_pwd)



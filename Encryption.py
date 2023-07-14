alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input("Typ encode to encrypt and decode to decypt: ")
text = input("enter the message: ").lower() #hello
shift = int(input("enter the number of times you need to shift: "))
# cipher_text = ' '
def encrypt(text,shift):
   cipher_text = ' '
   for i in range(len(text)):
    #   print(text[i])
      if text[i] in alphabet:
         index_num = alphabet.index(text[i])
         cipher_text += alphabet[index_num+shift]
      elif text[i] not in alphabet:
         cipher_text += text[i]   
        #  print(cipher_text)
   print(f"The encoded test is {cipher_text}")




def decrypt(cipher_text, shift):
      plain_text = ' '
      for i in range(len(cipher_text)):
        if cipher_text[i] in alphabet:
            index_num=alphabet.index(cipher_text[i])
            plain_text += alphabet[index_num-shift]

      print(f"The decoded test is {plain_text}")   

if direction == "encoded":         
    encrypt(text=text,shift=shift)  
elif direction == "decoded":     
    decrypt(cipher_text=text,shift=shift)    
else:
    print("no result found")      
    print("no result found")        




num = int(input("enter a number: "))
def primeNum(num):
   for i in range(2,num):
      if num%i==0:
         print("It's not a prime number")
      else:
         print("its a prime nmber")   

primeNum(num=num)                

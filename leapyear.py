def leapyear():
    year = int(input("enter a year: "))
    if(year%4==0):
        if(year%100==0):
            if(year%400==0):
                print("leap")
            else:
                print("not leap")
        else:
            print("leap")
    else:
        print("not leap") 



leapyear()                      

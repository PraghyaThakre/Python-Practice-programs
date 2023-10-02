def pizzorder():
    print("Welcome to the python Piza order application")
    size = input("What type of size do you need? S, M, L: ")
    add_pepperoni = input("add pepperoni yes, NO: ")
    add_cheese = input("add cheese yes, NO: ")
    small_pizza = 15
    medium_pizza = 20
    Large_pizza = 25
    if(size == "S"):
        if(add_pepperoni=="yes"):
            small_pizza += 2    
        if(add_cheese=='yes'):
            small_pizza += 1
        print(f"final prize of pizza {small_pizza}")
    elif(size == "M"):
        if(add_pepperoni=="yes"):
            medium_pizza += 3
        if(add_cheese=='yes'):
            medium_pizza += 1
        print(f"final prize of pizza {medium_pizza}")    
    else:
        if(add_pepperoni=="yes"):
            Large_pizza += 3
        if(add_cheese=='yes'):
            Large_pizza += 1
        print(f"final prize of pizza {Large_pizza}")    


pizzorder()
            
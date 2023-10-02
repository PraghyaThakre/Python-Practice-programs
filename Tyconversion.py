def typeconversion():
    two_dgt_num = input("Enter the two digit number\n")
    first_digit=two_dgt_num[0] #using subscript concept
    second_digit=two_dgt_num[1]
    result=int(first_digit)+int(second_digit)  #converting str into int for summation
    print(result)


typeconversion()    

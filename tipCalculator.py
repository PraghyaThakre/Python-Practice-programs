def tipCalculator():
    print("Welcome to the toip calculator")
    total_bill = input("What was the total bill? &")
    percentage_tip = input("What percentage tip would you like to give ? 10, 12 or 15?")
    actuatl_percentage_tip = int(percentage_tip)/100
    actual_total_bill = int(total_bill)*actuatl_percentage_tip
    final_bill = int(total_bill)+actual_total_bill
    num_people = input("How many people to split the bill?")
    contry_amt = final_bill/int(num_people)
    print(f"Each person should pay ${contry_amt}")


tipCalculator()    
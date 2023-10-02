def lifeInWeeks():
    age = input("What is your current age?")
    left_age = 90 - int(age)
    left_days = left_age*365
    left_weeks = left_age*52
    left_months = left_age*12
    print(f"you have {left_days} days, {left_weeks} weeks, {left_months} months")

lifeInWeeks()    

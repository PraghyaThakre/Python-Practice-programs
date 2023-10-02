def bmiCalculator():
    height = float(input("enter your height in m: "))
    weight = float(input("enter your weight in kg: "))

    BMI=weight/height**2
    BMI= round(BMI)
    if(BMI<18.5):
        print(f"your BMI is {BMI}, you are slightly underweight")
    elif(18.5<BMI<25):
        print(f"your BMI is {BMI}, you are normal weight")    
    elif(25<BMI<30):
        print(f"your BMI is {BMI}, you are slightly overweight")
    elif(30<BMI<35):
        print(f"your BMI is {BMI}, you are obese")
    else:
        print(f"your BMI is {BMI}, you are clinically obese")
        print("hello")

bmiCalculator()                    

import math

paint_h = int(input("enter the height of paint: "))
paint_w = int(input("enter the width of paint: "))
coverage = 5

def paint_cal(height,width,coverage):
   number_of_cans = math.ceil((height*width)/coverage) #ceil is for round up the number
   print(f"You will need {number_of_cans} paint")
   




paint_cal(height=paint_h,width=paint_w,coverage=coverage)    

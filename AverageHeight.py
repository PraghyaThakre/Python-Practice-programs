student_height = input("enter the list of student height:").split()
print(student_height)
total_h = 0
for h in student_height:
    total_h += int(h)

print(total_h)
total_number_of_h=0
# total_number_of_h = len(student_height) // using len function
for n  in student_height:  # using for loop counting the len of list
       total_number_of_h +=1

print(total_number_of_h)       
average_height = total_h//total_number_of_h # // double slash floor division concept for runding the value into exact integer format
print(average_height)

# print(round(average_height,2))


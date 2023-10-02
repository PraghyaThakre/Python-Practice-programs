students_score = input("provide the score of students: ").split()
print(students_score)
# students_score = int(students_score)
new_student_score = []
temp = ''
for n in range(0,len(students_score)):
      students_score[n] = int(students_score[n])

print(students_score) 
print(students_score.sort())     
heightest_score = 0
for score in students_score:
      if score >= heightest_score:
            heightest_score = score
            print(heightest_score)
            # new_student_score = heightest_score
            # print(new_student_score)

print("h is: "+ heightest_score)

# for score in students_score:
#       if score>= students_score:
#             new_student_score = score

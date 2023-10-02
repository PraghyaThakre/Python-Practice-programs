student_scores = {
    "Harry": 81,
    "ron": 78,
    "Hermione": 99,
    "draco": 74,
    "Neville": 62
}

student_grades = {}

for key in student_scores:
    if 91<=student_scores[key]<=100:
        print("Outstanding")
        student_grades[key] = "Outstanding"
    elif 81<=student_scores[key]<=90:
        print("Exceed Expectations")
        student_grades[key] = "Exceed Expectations"
    elif 71<=student_scores[key]<=80:
        print("Acceptable")
        student_grades[key] = "Acceptable"
    else:
        print("fail")        
        student_grades[key] = "Fail"

print(student_grades)        
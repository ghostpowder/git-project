number=input("""작업을 선택하세요.
    1. 입력
    2. 계산\n""")

if number == "1":
    num_subjects = int(input("과목 수를 입력하세요: "))
    total_grades = 0.0
    total_grades2=0.0
    submit_grade_points = 0.0
    view_grade_points = 0.0
    def gradepoint(grade):
        if grade == 'A+':
            return float(4.5)
        elif grade == 'A':
            return float(4.0)
        elif grade == 'B+':
            return float(3.5)
        elif grade == 'B':
            return float(3.0)
        elif grade == 'C+':
            return float(2.5)
        elif grade == 'C':
            return float(2.0)
        elif grade == 'D+':
            return float(1.5)
        elif grade == 'D':
            return float(1.0)
        else:
            return 0.0
           
        
    for i in range(num_subjects):
        grade = input("과목의 학점을 입력하세요 (A+, A, B+, B, C+, C, D+, D, F): ")
        score = float(input("과목의 평점을 입력하세요: "))
        print("입력되었습니다.")
        
        if grade != 'F':
            submit_grade_points += float(gradepoint(grade)) * score
            total_grades += score
            submit_gpa = total_grades / num_subjects
            
        view_grade_points += float(gradepoint(grade)) * score
        total_grades2 += score
        view_gpa = total_grades2 / num_subjects


print("제출용 :" +str(submit_grade_points )  + "학점 (gpa:"+str(submit_gpa)+ ")")
print("열람용 :" +str(view_grade_points ) + "학점 (gpa:"+str(view_gpa)+")")
print("프로그램을 종료합니다.")


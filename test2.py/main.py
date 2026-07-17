#Que 6
import json 
import student_utils
# print(student_utils.calculate_average(10,20,30))
students=[]
for i in range(3):
    name = input("Enter student name: ")
    print(name)
    marks=[]
    for j in range(3):
        while True:
            try:
                mark=float(input("Enter marks: "))
                if mark<0 or mark>100:
                    raise ValueError
                marks.append(mark)
                break 
            except:
                print("Invalid marks! Enter valid number")
    # print(mark) 
    avg = student_utils.calculate_average(*marks)
    grade=student_utils.get_grade(avg,pass_mark=40)
    print(name,avg,grade)
    students.append({
        "Name": name,
        "Average": avg,
        "Grade": grade
    })
with open("report.txt","w")as f:
    for student in students:
        f.write( f"Name: {student['Name']} | Average: {student['Average']:.2f} | Grade: {student['Grade']}\n"
        )
with open("students.json", "w") as f:
    json.dump(students, f, indent=4)
    
print("Contents of report.txt:")
with open("report.txt", "r") as fh:
    cont = fh.read()
    print(cont)
    
print("Content of students.json")
with open("students.json","r")as f:
    contt=f.read()
    print(contt)
    
print("Reading report.txt line by line")
with open("report.txt","r")as fh:
    read=fh.readlines()
    #print(read)
line=1
for i in read:
    print(line,i)
    line+=1
        
       
#Que 6
def get_grade(avg,pass_mark=40):
    if avg < pass_mark:
        return "Fail"
    elif avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    else:
        return "C"
#print(get_grade(67))
def calculate_average(*marks):
    a=sum(marks)
    b=len(marks)
    c=a/b
    return c 
print(calculate_average(10,20,30))
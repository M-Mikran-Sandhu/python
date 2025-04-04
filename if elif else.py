grade1=float(input("Input grade:"))
grade2=float(input("Input grade:"))

absences=int(input("Input absents:"))
total_classes = int(input("Total classes:"))

avg_grade=(grade1+grade2)/2
attendence=((total_classes-absences)/total_classes)*100
print("Average grade:",avg_grade)
print("Attendence rate:",attendence ,"%"
      )
if(avg_grade>=6):
    if(attendence>=80):
        print("Approved")
    else:
        print("Fail because of low attendence")
elif(attendence>=80):
    print("Fail because of low grade")
else:
    print("Fail because of low attendence and low grade")

#exercise error handling

data_valid=False

while data_valid==False:
    grade1= input("Enter grade:")
    try:
        grade1=float(grade1)
    except:
        print("Invalid input! Only numbers are accepted. Decimals should be seperated by a dot.")
        continue
    if grade1<0 or grade1>10:
        print("Grade must be Between 0 and 10")
        continue
    else:
        data_valid=True

data_valid=False

while data_valid == False:
    grade2=input("Enter grade:")
    try:
        grade2=float(grade2)
    except:
        print("Invalid input! Only numbers are accepted. Decimals should be seperated by a dot.")
        continue
    if grade2<0 or grade2>10:
        print("Grade must be between 0 and 10")
        continue
    else:
        data_valid=True
data_valid=False

while data_valid == False:
    attendence=input("Enter Attendence:")
    try:
        attendence=float(attendence)
    except:
        print("Invalid input! Only numbers are accepted. Decimals should be seperated by a dot.")
        continue
    if attendence<0 or attendence>50:
        print("Attendence must be between 0 and 50")
        continue
    else:
        data_valid=True

data_valid=False

while data_valid == False:
    Absences=int(input("Enter Absences:"))
    try:
        Absences=float(Absences)
    except:
        print("Invalid input! Only numbers are accepted. Decimals should be seperated by a dot.")
        continue
    if Absences<0 or Absences>attendence:
        print("Absences must be between 0 and ",attendence)
        continue
    else:
        data_valid=True


avg=(grade1+grade2)/2

total=(attendence-Absences)/attendence


print("Your Average Grade:",round(avg,2))
print("Your Attendence:",total*100,"%")

if avg>=6.0 and total>=0.8:
    print("Congrats! You have Passed")
elif avg<6.0 and total>=0.8:
    print("Sorry! You failed due to low Grades")
elif avg>=6.0 and total<0.8:
    print("Sorry! You failed due to low Attendence")
else:
    print("Sorry! You failed due to low Attendence and Grades")
    
    

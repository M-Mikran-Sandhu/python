weight=float(input("Enter Weight:"))
height=float(input("Enter Height:"))

bmi=weight/(height**2)

print("Your Body mass Index =",round(bmi,2))

if(bmi<18.5):
    print("You Are Under Weight")
elif(bmi>18.5 and bmi <24.9):
    print("You Are Normal Weight")
elif(bmi>24.9 and bmi>29.9):
    print("You Are Over Weight")
else:
    print("You Are Obesity")

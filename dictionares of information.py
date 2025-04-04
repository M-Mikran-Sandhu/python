person={"name":"Mikran Sandhu","gender":"male","age":20,"address":"Gujranwala","phone":+923217112944}
key=input("What information you want of the person (name,age,gender,address,phone):").lower()

result=person.get(key,"That information is not avaliable")
print( result )


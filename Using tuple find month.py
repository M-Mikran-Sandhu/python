birth=input("Enter your birthday as {DD-MM-YYYY}:")
month=int(birth[3:5])
month=month-1
months=("January","Feburary","March","April","May","June","July","Agust","Septumber","Octuber","November","December")
print("You were born in",months[month])

blog_post=["python","","cpp","","java"]

for  post in blog_post:
    if post=="":
        continue
    else:
        print(post)

print("________________________")

mystring="this is a string"

for char in mystring:
    print(char)
    
print("________________________")

for x in range(0,10):
    print(x)

print("________________________")

person={"Name":"Mikran","Age":10,"Gender":"male"}

for key in person:
    print(key, ":" ,person[key])
    
print("________________________")
blog_post={"one":["python","","cpp","","java"],"two":["python","","cpp","","java"]}

for cat in blog_post:
    print("Post no:",cat)
    for post in blog_post[cat]:
        if post =="":
            continue
        else:
            print(post)
    

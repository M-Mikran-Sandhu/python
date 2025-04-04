#functions

def say_hello(person):
    print("Hello", person ,",How are you")

say_hello( "mms")

def fahrtocelsius(fahr):
    celsius=(5*(fahr-32))/9
    return celsius

print("Celsius", round(fahrtocelsius(100),2))

def say_hello(person1,person2="mafia"):
    print("Hello", person1 ,",How are you",person2)

say_hello( "mms" ,"ucp")

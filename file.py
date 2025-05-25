with open("Myfile.txt","w") as f:
    f.write("Hello World\n")
    f.write("This is my first oython file")
    f.close()

with open("Myfile.txt","r") as f:
    content=f.read()
    print(content)
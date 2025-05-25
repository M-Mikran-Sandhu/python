class grade:
    def __init__(self, marks, name):
        self.name=name
        self.marks=marks

    def getGrade(self):

        self.marks = int(self.marks)
        if self.marks == 0:
            return "F"
        elif self.marks < 50:
            return "F"
        elif self.marks > 50 & self.marks < 60:
           return "D"
        elif self.marks > 60 & self.marks < 70:
            return "C"
        elif self.marks > 70 & self.marks < 80:
            return "B"
        elif self.marks > 80 & self.marks < 90:
            return "A"
        elif self.marks > 90 & self.marks < 100:
            return "A+"


s1=grade(90,"Mikran")
print("Grade for",s1.name,"Is: ",s1.getGrade())

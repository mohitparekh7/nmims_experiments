class Student:
    def getname(self,name):
        self.name=name
    def setname(self):
        print("Name:",self.name)
    def getid(self,id):
        self.id=id
    def setid(self):
        print("ID:",self.id)
    def getmarks(self,marks):
        self.marks=marks
    def setmarks(self):
        print("Marks:",self.marks)
    def calc(self):
        sum=0
        for i in self.marks:
            sum=sum+i
        p=(sum/(len(self.marks)*100))*100
        if(p>40):
            print("Passed")
            self.setname()
            self.setid()
            self.setmarks()
            print("Percentage:",p)
        else:
            print("Failed")


s=Student()
s.getname("mohit")
s.getid(29)
s.getmarks([99,98,66,90])
s.calc()


class employee:
    def __init__(self,name="",designation="",tele=""):
        self.name=""
        self.design = ""
        self.tele_no = []
    def setname(self,name):
        self.name = name
    def getname(self):
        print("NAME: ",self.name)
    def setdesign(self,designation):
        self.design=designation
    def getdesign(self):
        print("DESIGNATION: ",self.design)
    def settele_no(self,tele):
        self.tele_no=tele
    def gettele_no(self):
        print("TELEPHONE NO: ",self.tele_no)
    def validateempname(self,name):
        self.name=name
        if len(self.name)>3 :
            print("valid")
            self.getname()
            self.getdesign()
            self.gettele_no()
        else:
            print("invalid")
e = employee()
e.setname("MOHIT")
e.setdesign("head")
e.settele_no([7738281243])
e.validateempname("MOHIT")


class Online_Shopping:
    username = "mohit"
    password = "n029"
    u = input("enter username: ")
    p = input("enter password: ")
    menu = ["Electronics", "Clothes" ," shoes"]
    e_elec = {"Mobile" :10000 , "TV" :20000 , "Laptop":30000," Desktop":40000}
    e_men = {"formals":2000, "Casual" : 1000, "Traditional":5000}
    e_women = {"Punjabi":3000, "Formals":2000, "Western":1000}
    e_shoes = {"Formal":1000, "Casual":2000}
    e =0
    c2= 0
    a =0
    def create_bill(self):
        if (Online_Shopping.u == Online_Shopping.username) and (Online_Shopping.p == Online_Shopping.password):
            print(Online_Shopping.menu)
            x = int(input("enter your choice number: "))
            if(x == 1):
                print(Online_Shopping.e_elec)
                self.c1 = input("enter your choice ")
                Online_Shopping.a = self.c1
                Online_Shopping.c2 = Online_Shopping.e_elec.get(self.c1)
                Online_Shopping.e = input("enter quantity")
            elif(x==2):
                self.cho = input("men(m) or women(w)?")
                if (self.cho == 'm'):
                    print(Online_Shopping.e_men)
                    self.c1 = input("enter your choice")
                    Online_Shopping.a = self.c1
                    Online_Shopping.c2 = Online_Shopping.e_elec.get(self.c1)
                    Online_Shopping.e = input("enter quantity")

                elif (self.cho == 'w'):
                    print(Online_Shopping.e_women)
                    self.c1 = input("enter your choice")
                    Online_Shopping.a = self.c1
                    Online_Shopping.c2 = Online_Shopping.e_elec.get(self.c1)
                    Online_Shopping.e = input("enter quantity")

                else:
                    print("enter correct value")
            elif(x==3):
                print(Online_Shopping.e_shoes)
                self.c1 = input("enter your choice")
                Online_Shopping.a = self.c1
                Online_Shopping.c2 = Online_Shopping.e_elec.get(self.c1)
                Online_Shopping.e = input("enter quantity")
            else:
                print("enter correct value")
            # y = input("do you want to shop more ? (y/n)")
            # if(y == 'y'):
            #     Online_Shopping.create_bill()

        else:
            print("incorrect username and password combination!")

class billcal(Online_Shopping):
    def calc(self,total):
        self.total = total
        self.total = self.total*int(Online_Shopping.e)  * int(Online_Shopping.c2)
        print("Choose method of payment: ",["1. Paytm","2. Google Pay"])
        self.pay=int(input())
        if(self.pay==1):
            print("Amount deducted from Paytm wallet")
        elif(self.pay==2):
            print("Amount deducted from Bank account")
        else:
            print("Error")
        print("Details:")
        print("Item bought:",Online_Shopping.a)
        print("Quantity:",Online_Shopping.e)
        print("Total Bill:",self.total)


o = billcal()
o.create_bill()
o.calc(1)

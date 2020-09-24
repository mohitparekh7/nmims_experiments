import re
class recharge:
    def validate(self,s):
        self.pattern = re.compile('(0/91)?[7-9][0-9]{9}')
        return self.pattern.match(s)

    def check(self,no):
        self.ph = no
        if (int(self.ph[0]) == 9):
            print("vodafone user")
        elif (int(self.ph[0]) == 8):
            print("airtel user")
        else:
            print("jio user")
        print("Choose an option for recharge fom following:\n1. Full talktime \n2. Data pack \n3. Top up")
        self.ch = int(input("Select number:"))
        print("Choose a plan:\n1. 1000 \n2.500 \n3.101")
        self.pl = int(input("Select number:"))
        print("Choose payment method: \n1. Paytm \n2. Google Pay")
        self.p = int(input("Select number:"))

no = input("enter the mobile number")
o = recharge()
try:
    if(o.validate(no)):
        o.check(no)
    else:
        raise  Exception
except Exception as e:
    print("Invalid number")
else:
    print("Recharge sucessful")



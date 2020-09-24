class Airport:
    def check_baggage(self,baggage_weight):
        try:
            if (type(baggage_weight) != int):
                raise Exception
            else:
                if (baggage_weight >= 0 and baggage_weight <= 40):
                    return True
                else:
                    return False
        except Exception:
            print("Baggage Weight should be a number")

    def check_immigration(self, expiry_year):
        try:
            if (type(expiry_year) != int):
                raise Exception
            else:
                if (expiry_year >= 2001 and expiry_year <= 2025):
                    return True
                else:
                    return False
        except Exception:
            print("Expiry Year should be a number")

    def check_security(self, noc_status):
        try:
            if (type(noc_status) != str):
                raise Exception
            else:
                if (noc_status == 'valid' or noc_status == 'Valid'):
                    return True
                else:
                    return False
        except Exception:
            print("NOC status should be a string")

    def traveler(self):
        traveller_id = 1001
        traveler_name = 'Jim'
        d = self.check_baggage('Thirty')
        b = self.check_immigration(2016)
        c = self.check_security(0)
        if (d == 'True' and b == 'True' and c == 'True'):
            print("ID:", traveller_id)
            print("Name:", traveler_name)
            print("Allow traveler to fly")
        else:
            print("ID:", traveller_id)
            print("Name:", traveler_name)
            print("detain traveler for re-checking")


a = Airport()
a.traveler()

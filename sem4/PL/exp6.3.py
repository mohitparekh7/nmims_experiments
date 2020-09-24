class movie:
    theatre = ["PVR","INOX","CARNIVAL"]
    movie_name = ["A","B","C"]
    ticket_type = {"gold" : 45 ," recliner" : 20, "silver" : 40}
    price = {"gold" : 300 ," recliner" : 500, "silver" : 200}
    def booking(self):
        print("MOVIE : ",movie.movie_name)
        self.m = input("pick movie")
        print("theatre: ",movie.theatre)
        self.t = input("pick theatre")
        print("Seat Types: ",list(movie.ticket_type.keys()))
        self.type = input("Enter seat type you want: ")
        print("Corresponding no of seats:",list(movie.ticket_type.values()))
        self.no=int(input("Number of seats:"))
        if (self.no <= movie.ticket_type.get(self.type)):
            self.meal = input("Do you want a meal? Yes or No: ")
            if (self.meal == "Yes"):
                self.cost = (self.no * movie.price.get(self.type)) + 200
            else:
                self.cost = (self.no * movie.price.get(self.type))
            self.f = self.cost + (self.cost * 0.18)
        else:
            print("Error")
    def display(self):
        print("Details:")
        print("Movie Name:", self.m)
        print("Theatre:", self.t)
        print("Seat type:", self.type)
        print("Number of seats:", self.no)
        print("Opted for meal:", self.meal)
        print("Price:", self.f)

e = movie()
e.booking()
e.display()






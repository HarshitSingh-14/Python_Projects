##    --> OOPS used when : the program hava a lot of CODE

class RailwayForm:
        formType = "RailwayForm"
        
    
        def printData(self):
            print(f"Name is {self.name}")
            print(f"Train is {self.train}")


harshitsApplication = RailwayForm()
harshitsApplication.name ="Harshit"
harshitsApplication.train = "Rajdhani"
harshitsApplication.printData()
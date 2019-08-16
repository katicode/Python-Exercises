# -*- coding: cp1252 -*-

# class Competitor with 2 variables and 2 functions
class Competitor:
    color = ""
    points = 0
    def setInfo(self):
        self.color = input("Competitor's color? ")
        self.points = input("Competitor's points? ")
    def printInfo(self):
        print("Competitor",self.color,"have",self.points,"points!")

# main function		
def main():
    # creating a new instance of a class Competitor
    firstObject = Competitor()
    # ask color and points from user
    firstObject.setInfo()
    # print info
    firstObject.printInfo()

# Start program with main
if __name__ == "__main__":
    main()

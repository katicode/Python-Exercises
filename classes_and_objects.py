# -*- coding: cp1252 -*-

# class Competitor with 2 variables and 3 functions
class Competitor:
    color = ""
    points = 0
    def setInfo(self):
        self.color = input("Competitor's color? ")
    def printInfo(self):
        print("Competitor",self.color,"have",self.points,"points!")
    def goal(self):
        self.points = +1
        print("Competitor",self.color,"scored a goal!")

# main function		
def main():
    # creating a new instance of a class Competitor
    firstObject = Competitor()
    # ask color from user
    firstObject.setInfo()
    # print info
    firstObject.printInfo()
    # firstObject scored a goal
    firstObject.goal()
    # print info
    firstObject.printInfo()

# Start program with main
if __name__ == "__main__":
    main()

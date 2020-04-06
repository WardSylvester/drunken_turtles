# -- This is an iteration of code done for CSC 500 at UNCW for the final project -- Drunken Turtles

# -- importing relevant libraries
import random
import turtle
import math
import time

# -- This is creating a new class called Drunk. It is inheriting functionality from the Turtle class and thus is a
# -- subclass of the Turtle class. It has a randomly initiated position but done so in ranges of 40 so that it always
# -- starts the center of a grid. It also has initiated y and x coordinate values and has destination y and x values
# -- that can be used to calculate the distance traveled.
class Drunk(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.speed = 0
        self.penup()
        self.setposition(random.randrange(-400, 400, 40), random.randrange(-400, 400, 40))
        self.pendown()
        self.dot(5, 'black')
        self.shape('turtle')
        self.pensize(3)
        self.pencolor('red')
        self.homeY = self.setY()
        self.homeX = self.setX()
        self.destinationX = self.destX()
        self.destinationY = self.destY()
        self.moves = 0

# -- This method chooses a random angle in 45 degree increments and sets the heading of the object to that angle as well
# -- as returning that value so that it can be used by other functions
    def setAngle(self):
        angle = [0, 45, 90, 135, 180, 225, 270, 315]
        angle2 = angle[random.randint(0, 7)]
        self.setheading(angle2)
        return angle2

# -- This function is what moves the object. The object moves in increments of 40. It also keeps track of the number of moves the object has made. 
    def move(self):
            self.forward(25)
            self.moves += 1
            

# -- the following methods allow the programmer to set new values to the home and destination coordinates as well as
# -- return those values if need be.
    def setX(self):
        homeX = self.xcor()
        return homeX

    def setY(self):
        homeY = self.ycor()
        return homeY

    def destX(self):
        destX = self.xcor()
        return destX

    def destY(self):
        destY = self.ycor()
        return destY

    def setDestX(self):
        self.destinationX = self.destX()

    def setDestY(self):
        self.destinationY = self.destY()

    def returnHomeX(self):
        return self.homeX

    def returnHomeY(self):
        return self.homeY

    def returnDestX(self):
        return self.destinationX

    def returnDestY(self):
        return self.destinationY

    def returnMove(self):
        return self.moves
    

# -- This method is used to calculate the distance between the two points of the object -- Its home coordinates which
# -- are set when the object is initiated and its destination coordinates which are updated every time it moves.
    def calcDistance(self):
        distance = math.sqrt(((self.destinationX - self.homeX)**2) + ((self.destinationY - self.homeY)**2))
        return distance

# -- This function simply draws the distance between its home and destination coordinates in blue
    def DrawDistance(self):
        self.penup()
        self.goto(self.homeX, self.homeY)
        self.pencolor("blue")
        self.pendown()
        self.goto(self.destinationX, self.destinationY)
        self.penup()

# -- These functions are taken from the bouncing balls example in our book and stop the Drunk objects from going outside
# -- of the grid. There is one small change of an additional + or -1. This is to fix a bug caused by the computer being
# -- very accurate and not rounding. It would take something like 399.9999 as not being on 400 and would allow the Drunk
# -- object to leave the grid
    def atLeftEdge(self, screen_width):
        if (self.xcor() - 40) <= ((-screen_width / 2) + 1):
            return True
        else:
            return False

    def atRightEdge(self, screen_width):
        if (self.xcor() + 40) >= ((screen_width / 2) - 1):
            return True
        else:
            return False

    def atTopEdge(self, screen_height):
        if (self.ycor() + 40) >= ((screen_height / 2) - 1):
            return True
        else:
            return False

    def atBottomEdge(self, screen_height):
        if (self.ycor() - 40) <= ((-screen_height / 2) + 1):
            return True
        else:
            return False

# -- This function sets the amount of moves the player would like and does so in an error catching way
def setSeconds():
    flag = True
    print('Hello User! You can choose how long the program runs in a number of seconds,')
    print('but be aware that we have limited the time up to 5 minutes or 300 seconds.')
    print()
    while flag:
        try:
            seconds = int(input("Please, enter a number of seconds for program to run: "))
            if seconds > 0 and seconds<(60*5):
                flag = False
            else:
                print("Ups! I bet, the number you have entered is out of the acceptable range! Let's try again!")
                print()
        except:
            print("Ups! I bet, it is not even a number! Let's try again!")
            print()
    return seconds

# -- This function sets the "key" or how many creatures the user wants and does so in an error catching way.
def setKey():
    flag = True
    print('Well done! Now you can choose how much drunken turtles will be running around!')
    print('There is a reasonable limit of 15 turtles that can fit to our little swimming pool.')
    print()
    while flag:
        try:
            key = int(input("Please, enter a number of turtles (Max = 15): "))
            if key > 0 and key < 16:
                flag = False
            else:
                print("Ups! I bet, the number you have entered is out of the acceptable range! Let's try again!")
                print()
        except:
            print("Ups! I bet, it is not even a number! Let's try again!")
            print()
    return key

# -- This function adds together all the distances that the turtles traveled.
def calc_total_dist(creatures):
    total_dist = 0
    for x in creatures:
        total_dist += (Drunk.calcDistance(x))
    return total_dist

# -- This function calculates the average distance traveled of all the turtles.
def calc_avg_dist(creatures):
    total_dist = 0
    for x in creatures:
        total_dist += (Drunk.calcDistance(x))
    avg_dist = total_dist/len(creatures)
    return avg_dist

def calc_total_moves(creatures):
    total_moves = 0
    for x in creatures:
        total_moves += (Drunk.returnMove(x))
    return total_moves

# -- Main --

print()
print('-'*60)
print("This program simulates a random (Drunkard's) Walk")
print('-'*60)
print()

# -- These functions capture the amount of seconds and amount of creatures the user wants
seconds = int(setSeconds())
print()
key = int(setKey())
print()
print("Great! Let's Rock'n'Roll it!")
print()

# -- This sets up the windows an even 800 by 800
turtle.setup(800, 800)
screen_width = 800
screen_height = 800
window = turtle.Screen()
turtle.hideturtle()
turtle.bgpic("water.gif")
window.title('Drunk Turtles')
drunkTurtle = turtle.getturtle()

# -- This creates the grid in the same window we previously created
#grid(drunkTurtle, window)

# -- This creates an empty list -- creatures. It then iterates using a for loop in range from 0 to the "key" or
# -- the amount of creatures the player wants to be created. Each loop it iterates a new instance of the Object "Drunk".
# -- The objects are initialized at random on the board.
creatures = []
for k in range(0, key):
    creatures.append(Drunk())

# -- This creates the movement of the creatures. For range of 0 to the amount of seconds the user wants to goes through
# -- each Drunk object in the creature list one at a time. It generates a random angle and then checks the creature to
# -- see if the creature is on an edge. If it is on an edge it changes the angle to the opposite direction of the edge
# -- and then moves. If it is not on an edge it moves based on the random angle generated initially. It also sets the
# -- destination value in each object to the new location it has moved too.

# -- set start time
start_time = time.time()

# -- variable used to stop movement when number of seconds reached
terminate = False

while not terminate:
        for b in creatures:
            i = Drunk.setAngle(b)
            if Drunk.atLeftEdge(b, screen_width):
                b.setheading(0)
                Drunk.move(b)
                Drunk.setDestX(b)
                Drunk.setDestY(b)
            elif Drunk.atRightEdge(b, screen_width):
                b.setheading(180)
                Drunk.move(b)
                Drunk.setDestX(b)
                Drunk.setDestY(b)
            elif Drunk.atTopEdge(b, screen_height):
                b.setheading(270)
                Drunk.move(b)
                Drunk.setDestX(b)
                Drunk.setDestY(b)
            elif Drunk.atBottomEdge(b, screen_height):
                b.setheading(90)
                Drunk.move(b)
                Drunk.setDestX(b)
                Drunk.setDestY(b)
            else:
                Drunk.move(b)
                Drunk.setDestX(b)
                Drunk.setDestY(b)
            if time.time() - start_time > seconds:
                terminate = True

# -- This function then iterates through each Drunk object in the list creatures and uses the DrawDistance function
# -- to draw a blue line from its starting point to its final destination.
for c in creatures:
    Drunk.DrawDistance(c)

# -- This puts all data for each creature in list to make it easier to print in table form
e = 1
creature_data = [['Turtle','Start x','Start y','End x','End y','Distance Traveled','Moves Made']]
for d in creatures:
    lst = ['Turtle_'+ str(e),(Drunk.returnHomeX(d)),(Drunk.returnHomeY(d)),(Drunk.returnDestX(d)),(Drunk.returnDestY(d)),(Drunk.calcDistance(d)),(Drunk.returnMove(d))]
    creature_data.append(lst)
    e += 1

# -- This prints out the starting x and y coordinates and the ending x and y coordinates as well as the distance
# -- travelled by the creature at the end, total distance traveled by all turtles, and average distance traveled
print("\n\n")
print("Data for program run for " + str(seconds) + " seconds and with " + str(key) + " creature(s):")
dash = '-' * 80

for i in range(len(creature_data)):
    if i == 0:
      print(" ")  
      print(dash)
      print('{:<4s}{:>14s}{:>9s}{:>9s}{:>9s}{:>20s}{:>12s}'.format(creature_data[i][0],creature_data[i][1],creature_data[i][2],creature_data[i][3],creature_data[i][4],creature_data[i][5],creature_data[i][6]))
      print(dash)
    else:
      print('{:<6s}{:>10.1f}{:>10.1f}{:>10.1f}{:>10.1f}{:>11.1f}{:>14.1f}'.format(creature_data[i][0],creature_data[i][1],creature_data[i][2],creature_data[i][3],creature_data[i][4],creature_data[i][5],creature_data[i][6]))

print('\nTotal Distance Traveled: ' + str('%.2f' % calc_total_dist(creatures)))
print('Average Distance Traveled: ' + str('%.2f' % calc_avg_dist(creatures)))
print('Total Moves Made: ' + str(calc_total_moves(creatures)))

   
# -- This makes it so the turtle window only closes after a click and will stay open for observation until that has
# -- happened.
window.exitonclick()

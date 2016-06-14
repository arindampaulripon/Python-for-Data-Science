import Turtle

# Each of the command classes below hold information for one of the types of comands found in a graphics file. For each
# command there must be a draw method that is given to a turtle and uses the turtle to draw the object. By having
# a draw method for each class, we can polymorphically call the right draw method when traversing a sequence of these
# commands. Polymorphism occurs when the "right" draw method gets called without having to know which graphics command
# it is being called upon.


class GoToCommand:
    # Here the constructor is defined with default values for width and color. This means we can construct a GoToCommand
    # objects as GoToCommand(10,20), or GoToCommand(10,20,5) or GoToCommand(10,20,5"yellow).
    def __init__(self, x, y, width = 1.0, color = "black"):
        self.x = x
        self.y = y
        self.color = color
        self.width = width

    def draw(self, turtle):
        Turtle.width(self.width)
        Turtle.pencolor(self.color)
        Turtle.goto(self.x, self.y)


class CircleCommand:
    def __init__(self, radius, width = 1.0, color = "black"):
        self.radius = radius
        self.width = width
        self.color = color

    def draw(self, turtle):
        Turtle.width(self.width)
        Turtle.pencolor(self.color)
        Turtle.circle(self.radius)


class BeginFillCommand:
    def __init__(self, color):
        self.color = color

    def draw(self, turtle):
        Turtle.fillcolor(self.color)
        Turtle.begin_fill()


class EndFillCommand:
    def __init__(self):
        # Pass is a statement placeholder and does nothing. We have nothing to initialize in this class because all we
        # want is the polymorphic behavior of the draw method.
        pass

    def draw(self, turtle):
        Turtle.end_fill()


class PenUpCommand:
    def __init__(self):
        pass

    def draw(self, turtle):
        Turtle.penup()


class PenDownCommand:
    def __init__(self):
        pass

    def draw(self, turtle):
        Turtle.pendown()

# This is our PyList class. It holds a list of our graphics commands.


class PyList:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items = self.items + [item]

    def __iter__(self):
        for c in self.items:
            yield c


def main():
    filename = input("Please enter drawing filename: ")

    t = Turtle.Turtle()
    screen = t.getscreen()
    file = open(filename, "r")

    # Create a PyList to hold the graphics commands that are read from the file.
    graphicsCommands = PyList()

    command = file.readline().strip()

    while command != "":

        # Now we must read the rest of the record and then process it. Because records are variable length, we'll use
        # if-elif to determine which type of record it is and then we'll read and process the record.

        if command == "goto":
            x = float(file.readline())
            y = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            cmd = GoToCommand(x, y, width, color)
        elif command == "circle":
            radius = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            cmd = CircleCommand(radius, width, color)
        elif command == "beginfill":
            color = file.readline().strip()
            cmd = BeginFillCommand(color)
        elif command == "endfill":
            cmd = EndFillCommand()
        elif command == "penup":
            cmd = PenUpCommand()
        elif command == "pendown":
            cmd = PenDownCommand()
        else:
            raise RuntimeError("Unknown command found in file: " + command)

        # Finish processing the record by adding the command to the sequence.
        graphicsCommands.append(cmd)

        # Read one more line to set up for the next time through the loop
        command = file.readline().strip()

    # This code iterates through the commands to do the drawing and demonstrates the uses of the __iter(self)__ method
    # in the PyList class above.
    for cmd in graphicsCommands:
        cmd.draw(t)

    file.close()
    t.ht()
    screen.exitonclick()
    print("Program Execution Completed.")

if __name__ == "__main__":
    main()
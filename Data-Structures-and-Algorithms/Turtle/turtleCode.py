# Imports always at the top.
# The unsafe way of importing a module in Python:
# from turtle import *
# t = Turtle()
# The correct/safe way to do it is:

import Turtle

# Other function definitions followed by the main function definition
def main():
    # The main code of the program goes here

    # This line reads a line of input from the user.
    filename = input("Please enter drawing filename: ")

    # Create a Turtle Graphics window to draw in.
    t = Turtle.Turtle()
    # The screen is used at the end of the program.
    screen = t.getscreen()

    # The next line opens the file for "r" or reading. "w" would open it for writing, and "a" would open the file to
    # append to it (i.e. add t the end). In this program we are only interested in reading the file.
    commandFile = open(filename, "r")

    # The following for loop reads the lines of the file, one at a time and executes the body of the loop once for each
    # line of the file.
    for line in commandFile:

        # The strip method strips of the newline character at the end of the line and any blanks that might be at the
        # beginning or end of the line.
        text = line.strip()

        # The following line splits the text variable into its pieces. For instance, if text contained "goto, 10, 20, 1
        # , black" then commandList will be equal to ["goto", "10", "20", "1", "black"] after splitting the text.
        commandList = text.split(",")

        # get the drawing command
        command = commandList[0]

        if command == "goto":
            # Writing float(commandList[1]) makes a float object out of the string found in commandList[1]. You can do
            # similar conversion between types for int objects.
            x = float(commandList[1])
            y = float(commandList[2])
            width = float(commandList[3])
            color = commandList[4].strip()
            t.width(width)
            t.pencolor(color)
            t.goto(x, y)
        elif command == "circle":
            radius = float(commandList[1])
            width = float(commandList[2])
            color = commandList[3].strip()
            t.width(width)
            t.pencolor(color)
            t.circle(radius)
        elif command == "beginfill":
            color = commandList[1].strip()
            t.fillcolor(color)
            t.begin_fill()
        elif command == "endfill":
            t.end_fill()
        elif command == "penup":
            t.penup()
        elif command == "pendown":
            t.pendown()
        else:
            print("Unkown command found in file:", command)

    # Close the file
    commandFile.close()

    # Hide the turtle that we used to draw the picture.
    t.ht()

    # This causes the program to hold the turtle graphics window open until the mouse is clicked.
    screen.exitonclick()
    print("Program Execution Completed.")

# This code calls the main function to get everything started.
if __name__ == "__main__":
    main()


# This code calls the main function to get everything started. The condition in this if statement evaluates to True
# when the module is executed by the interpreter. But not when it is imported into another module.
if __name__ == "__main__":
    main()
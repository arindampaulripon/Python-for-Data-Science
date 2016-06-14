import Turtle
def main():
    filename = input("Please enter drawing filename: ")

    t = Turtle.Turtle()
    screen = t.getscreen()

    file = open(filename, "r")

    # Here we have the half a loop to get things started. Reading our first graphics command here lets us determine if
    # the file is empty or not.
    command = file.readline().strip()

    # If the command is empty, then there are no more commands left in the file.
    while command != "":

        # Now we must read the rest of the record and then process it. Because records are variable length, we'll use
        # if-elif to determine which type of record it is and then we'll read and process the record.

        if command == "goto":
            x = float(file.readline())
            y = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            t.width(width)
            t.pencolor(color)
            t.goto(x,y)
        elif command == "circle":
            radius = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            t.width(width)
            t.pencolor(color)
            t.circle(radius)
        elif command == "beginfill":
            color = file.readline().strip()
            t.fillcolor(color)
            t.begin_fill()
        elif command == "endfill":
            t.end_fill()
        elif command == "penup":
            t.penup()
        elif command == "pendown":
            t.pendown()
        else:
            print("Unknown command found in file:", command)

        command = file.readline().strip()

    # Close the file
    file.close()

    t.ht()
    screen.exitonclick()
    print("Program Execution Completed.")

if __name__ == "__main__":
    main()
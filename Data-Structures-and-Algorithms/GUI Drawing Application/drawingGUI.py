# This class defines the drawing application. The following line says that the drawing class inherits from the Frame
# class. This means that the DrawingApplication is like a Frame object except for the code written here which redefines
# and extends the behavior of a Frame.

class DrawingApplication(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        self.buildWindow()
        self.graphicsCommands = PyList()

    # This method is called to create all the widgets, place them in the GUI, and define the event handlers for the app.
    def buildWindow(self):

        # The master is the root window. The title is the set as below.
        self.master.title("Draw")

        # Here is how to create a menu bar. The tearoff = 0 means that the menus can't be separated from the window
        # which is a feature of tkinter.
        bar = tkinter.Menu(self.master)
        fileMenu - tkinter.Menu(bar, tearoff = 0)
        
        # This code is called by the "New" menu item below when it is selected.
        # The same applies for loadFile, addToFile, and saveFile below. The
        # "Exit" menu item below calls quit on the "master" or root window.
        def newWindow():
            # This sets up the turtle to be ready for a new picture to be drawn. 
            # It also sets the sequence back to empty. It is necessary for the
            # graphicsCommands sequence to be in the objsect (i.e. self.graphicsCommands)
            # because otherwise the statement:
            # graphicsCommands = PyList()
            # would make this variable a local variable in the newWindow method. If it were
            # local, it would not be set anymore once the newWindow method returned.
            theTurtle.clear()
            theTurtle.penup()
            theTurtle.goto(0,0)
            theTurtle.pendown()
            screen.update()
            screen.listen()
            self.graphicsCommands = PyList()
            
        fileMenu.add_command(label="New", command=newWindow)
        
        # The parse function adds the contents of an XML file to the sequence.
        def parse(filename):
            xmldoc = xml.dom.minidom.parse(filename)
            
            graphicsCommandsElement = xmldoc.getElementsByTagName("graphicsCommands")[0]
            graphicsCommands = graphicsCommandsElement.getElementsByTagName("command")
            
            for commandElement in graphicsCommands:
                print(type(commandElement))
                command = commandElement.firstChild.data.strip()
                attr = commandElement.attributes
                if command == "GoTo":
                    x = float(attr["x"].value)
                    y = float(attr["y"].value)
                    width = float(attr["width"].value)
                    color = attr["color"].value.strip()
                    cmd = GoToCommand(x,y,width,color)
                    
                elif command == "Circle":
                    
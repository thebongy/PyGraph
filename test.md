# PyGraph User Guide

## System Requirements

Windows XP or above with Python 2.7 installed.

## How to use PyGraph?

The Application can be used to view the shape of various graphs, and is
not a completely accurate representation of the graph.

You can navigate the Application using the ARROW keys, and options can
be selected by pressing the ENTER key.

To graph an equation, first move in the Graph menu from the main menu,
and then type the mathematical expression in the textbox that shows.

Press Enter to then graph the expression.

If your expression has no errors, then you should be moved to the graph
view. Here are the controls for the graphing view:

\----------------------------------------------------

KEY ACTION

z Zoom out

Z Zoom in

x Zoom out x-axis

X Zoom in x-axis

y Zoom out y-axis

Y Zoom in y-axis

r Reset to Initial View

Arrow Keys Move around graph

\---------------------------------------------------

Have Fun Graphing\!

# PyGraph Documentation

## 

## Project Directory Structure:

  - src/

<!-- end list -->

  - main.py: The main application file which is run by the user.

  - display/
    
      - about.txt: Text file with contents of the about menu of the
        application
    
      - help.txt: Text file with contents of the help menu of the
        application
    
      - logo.txt: Text file with main screen ASCII logo of the app
    
      - inputhandler.py: Raises events based on user input.
    
      - menu.py: Handles displaying of various menus of the app

  - postfix/
    
      - stack.py: Defines a class for managing a LIFO list.
    
      - components.py: Defines various components of a mathematical
        expression: Functions, Operators, etc.
    
      - constants.py: Defines mathematical constants like pi, e, etc.
    
      - functions.py: Defines mathematical functions like sin, cos, tan,
        etc.
    
      - operators.py: Defines mathematical operators like +,-,\*,/,etc.
    
      - parser.py: Handles string expression to postfix conversions

  - render/
    
      - EventManager.py: Registers objects as event listeners, and
        manages notification of object events.
    
      - terminal.py: Handles terminal commands like clearing, resizing
        the screen.
    
      - utils.py: Handles the 2D lists for various components on the
        screen.

## Code Structure

The code employs a Model-View-Controller (MVC) architecture


## The Event Manager


The majority of the code consists of over 40 classes, and communication
between components of code can get messy if not handled properly. This
was solved by defining an Event Manager. The code flow is majorly
controlled through the Event Manager. The **Event Manager** class
defined two important methods:

1.  .registerListener(object, event) : Registers an object as a listener
    for an event.

2.  .update(event): Notifies all event listeners that an event is
    occuring.

An example of this in action, is the communication between the
controller and the view. The classes related to the view register
themselves to listen to events like ArrowKeyEvent, EnterKeyEvent, etc.
When the user presses the enter key, for example, the controller class
updates the EventManager class about the EnterKeyEvent, which then in
turn notifies all listeners of the EnterKeyEvent about the event, which
are then able to do the required actions to update the view.

Here is a list of such event classes defined in the program:

1.  **ArrowKey()**

2.  **EnterKey()**

3.  **EscapeKey()**

4.  **BackSpace()**

5.  **KeyPress()**

6.  **OptionSelectedEvent(*code)<sup>\*</sup>***

7.  **OptionHighlightedEvent(*code*)<sup>\*</sup>**

8.  **DisplayMainMenu()**

\* The code attributes is used to identify which option was selected on
a menu screen.

## <span class="underline"></span>

## <span class="underline">Interpreting Mathematical Expressions</span>


The program first converts the string expression into a list of
mathematical units implemented as Python Objects. Each of these
mathematical units is a subclass of the Unit Class:

> **Unit(*data, start, end)*:**

1.  data: the mathematical unit as a raw string.

2.  start: the starting index of the unit in the real string expression.

3.  end: the ending index of the unit in the real string expression.

The child classes of Unit are the following:

1.  **Operator(func, priority)**
    
    1.  <span class="underline">Func</span>: A function which takes the
        operands as arguments, and returns the result of the operator.
    
    2.  <span class="underline">Priority</span>: (Int) Lower the value,
        means the operator has higher precedence.

2.  **UnaryOperator()** (*Child of Operator)*

3.  **BinaryOperator()** (*Child of Operator)*

4.  **Constant(val)**
    
    3.  *<span class="underline">Val:</span> The value of the constant*

5.  **Variable()**

6.  **Function(func, expr)**
    
    4.  <span class="underline">func</span>: A function which returns
        the result of the required mathematical function.
    
    5.  <span class="underline">expr</span>: The argument of the
        function, as an *Expression* object.

7.  **Parenthesis(type, depth)**
    
    6.  <span class="underline">Type:</span> Either “(“ or “)”
    
    7.  <span class="underline">Depth</span>: an integer, representing
        the how many parenthesis is the current parenthesis inside. This
        value is used to determine whether the expression entered is
        valid.

Each of the above units defines the *.evaluate()* method, which returns
a numerical value after evaluating the Operator/Function/Variable etc.

The conversion from string to a list of mathematical units is done by
the ObjectRepresentation() class.

> **ObjectRepresentation(expr)**

1.  <span class="underline">expr:</span> The math expression as a raw
    string.

> Methods:

1.  <span class="underline">construct()</span>: Constructs the string
    expression into a python list of the units defined above. The list
    is stored in the instance variable *expression.*

The list representation of the expression is now converted into a
postfix representation by the postfix class:

> **Postfix(expr)**

1.  expr: The list representation of the math expression generated by
    ObjectRepresentation().

> Methods:

1.  <span class="underline">construct\_postfix():</span> Generates the
    postfix expression from expr and stores it in the instance variable
    *postfix.*

2.  <span class="underline">evaluate(x)</span>: Evaluates the postfix
    expression for a value of x.

The *Expression* class unifies the job of the ObjectRepresentation() and
Postfix() classes by calling them both in its constructor, and thus
serves as a placeholder class to represent a mathematical expression,
and provides methods to evaluate the same.

> **Expression(expr)**

1.  <span class="underline">Expr:</span> The math expression as a
    string.

2.  <span class="underline">Postfix</span>: Instance variabe which
    stores the Postfix() object for expr.

> Methods:

1.  <span class="underline">evaluate(x)</span>: Calls
    self.postfix.evaluate(x).

## <span class="underline">The Graphical User Interface</span>

PyGraph makes use of just the command prompt for all of its menus. It
does this by maintaining the CMD window’s viewport as a 2D list, and
then constructs components on this 2-D list one by one, and the finally
prints this 2D list on the screen. Before a print cycle, the program
also clears the existing screen. The clear + print process happens in
under 0.4s, creating the effect to the user that the display is instant.

## 

## <span class="underline">Surfaces and Rects</span>

PyGraph represents all its components on screen as separate 2D lists. It
defines a basic class, known as *Surface*. This class stores the 2D list
of the graphical component of the screen, and also provides the .draw()
method, to draw other *Surface* objects on this *Surface* object.

> **Surface(tl, data):**

1.  <span class="underline">tl</span>: The topleft coordinate of this
    surface object respective to the terminal screen.

2.  <span class="underline">Data</span>: A 2D List representing the data
    of the surface.

> Methods:

1.  <span class="underline">draw(*surface*):</span> Draws the argument
    *surface* on current surface’s data instance atrribute.

The Surface Class also stores another instance variable called *rect,*
which stores positional data about the current surface as a *Rect*
object:

> **Rect(pos, size):**

1.  <span class="underline">pos</span>: TopLeft Coordinate of the rect

2.  <span class="underline">Size</span>: width and height of the rect

> Using the above two parameters, the Rect calculates all its other
> instance arguments:

1.  <span class="underline">Tl</span>: top left coordinate

2.  <span class="underline">Tr</span>: top right coordinate

3.  <span class="underline">Bl</span>: bottom left coordinate

4.  <span class="underline">Br</span>: Bottom right coordinate

5.  <span class="underline">Left</span>: Left abcissa

6.  <span class="underline">Right</span>: Right abcissa

7.  <span class="underline">Top</span>: Top ordinate

8.  <span class="underline">Bottom</span>: Bottom ordinate

9.  <span class="underline">Center:</span> Center coordinate

> Methods:

1.  <span class="underline">inRect(Point)</span>: Checks whether the
    Point lies inside the Rect.

The Surface class has various children, each defining a different GUI
Components/Widget:

1.  **Text()**: Represents any text to display on the screen.

> Methods:

1.  <span class="underline">Highlight():</span> Underline the Text

2.  <span class="underline">UnHighlight():</span> Remove any underlines
    from the text.

<!-- end list -->

2.  **Rectangle()**: Draws a rectangle on the screen.

3.  **Paragraph():** Similar to the Text() class, except has more
    features for wrapping words correctly in long passages of text and
    preventing display bugs like words going out of screen,

4.  **InputBox()**: Implements a rectangular input box on the screen.

> Methods:

1.  <span class="underline">input(char):</span> Enters a single
    character *char* in the inputbox.

2.  <span class="underline">backSpace()</span>: Removes the latest char
    from the inputbox

3.  <span class="underline">clearInput()</span>: Clears the InputBox.

The Program also defines another Surface Object called Terminal() which
represents the command prompt screen, and provides several extra methods
for controlling the command prompt window:

> **Terminal(size)**
> 
> Instance Attributes:

1.  <span class="underline">size</span>: Tuple representing the width
    and height of the cmd window.

> Methods:

1.  <span class="underline">update\_screen()</span>: Prints the
    terminal’s surface data on the screen.

2.  <span class="underline">Clear\_data()</span>: Clears the terminal’s
    data list.

3.  <span class="underline">Clear\_screen()</span>: Clears the terminal
    screen with the cls command.

4.  <span class="underline">Resize\_screen():</span> Resizes the cmd
    screen.

## <span class="underline">Menus</span>

The different menu screens are all child classes of one main class:
MainContent(). This class defines a basic view on the screen, by drawing
a simple border around the screen with Rectangle(), and also provides
important methods for updating the display, and showing it on the
screen,

> **MainContent(title, ev, terminal):**

1.  <span class="underline">Title</span>: The title text for the current
    menu.

2.  <span class="underline">Ev</span>: The EventManager object of the
    program.

3.  <span class="underline">Terminal</span>: The terminal surface object
    of the program.

> Other Instance Attributes:

1.  <span class="underline">Showing</span>: *True* if the menu is
    current showing on the screen, False otherwise.

2.  <span class="underline">titleSurface</span>: The Text Surface Object
    for the title text.

3.  <span class="underline">mainBorder</span>: The Rectangle Surface
    Object for the menu.

4.  <span class="underline">contentSize:</span> The size of the main
    content area inside the border as a (width, height) tuple.

5.  <span class="underline">content:</span> A Surface representing the
    content to draw inside the screen.

6.  <span class="underline">Misc</span>: A list representing
    miscellaneous surfaces to draw on the screen.

> Methods:

1.  <span class="underline">display():</span> Draws titleSurface,
    mainBorder, content, and all surfaces in Misc on the Terminal
    Surface object.

2.  <span class="underline">update():</span> Abstract Method, called
    when a menu’s data has to be updates because of some user
    interaction.

The MainContent class has several children, each defining their own menu
to display on the screen:

1.  **MainMenu**: The Menu which shows when the program is opened.

2.  **EquationInput**: The menu screen where the mathematical expression
    is input.

3.  **Graph**: The menu screen which displays the graph and allows the
    user to navigate around it.

4.  **Help:** The Help Menu.

5.  **About**: THe About Menu.

## <span class="underline">User Input</span>

User inputs is handled by the **inputhandler()** function. This function
uses the getch() function from the msvcrt module to catch a single
keypress by the user. It then interprets the keycode returned by the
getch function() and then appropriately raises an event to the
EventManager class relating to the key pressed.


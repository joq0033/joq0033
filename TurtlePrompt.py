from TurtleDrawer import TurtleDrawer
from Parser import IntegerParser, StringParser
from cmd import Cmd


class TurtlePrompt(Cmd):
    welcome = "Welcome to Turtle Shell"
    prompt = '(turtle)'
    file = None

    def do_P(self, arg):
        """Select Pen:  P 10"""
        data = IntegerParser.parse(self, arg)
        TurtleDrawer.select_pen(self, data)

    def do_U(self, arg):
        """Pen Up : U"""
        command = StringParser.parse(self, arg)
        TurtleDrawer.pen_up(command)

    def do_D(self, arg):
        """Pen Down : D"""
        command = StringParser.parse(self, arg)
        TurtleDrawer.pen_down(command)

    def do_X(self, arg):
        """Go Along : X 100"""
        command = IntegerParser.parse(self, arg)
        TurtleDrawer.go_along(self, command)

    def do_Y(self, arg):
        """Go Down : Y 100"""
        command = IntegerParser.parse(self, arg)
        TurtleDrawer.go_down(self, command)

    def do_N(self, arg):
        """Draw line 0 degrees : N 100"""
        command = IntegerParser.parse(self, arg)
        TurtleDrawer.draw_line(self, 0, command)

    def do_E(self, arg):
        """Draw line 90 degrees : E 100"""
        command = IntegerParser.parse(self, arg)
        TurtleDrawer.draw_line(self, 90, command)

    def do_S(self, arg):
        """Draw line 120 degrees : S 100"""
        command = IntegerParser.parse(self, arg)
        TurtleDrawer.draw_line(self, 180, command)

    def do_W(self, arg):
        """Draw line 270 degrees : W 100"""
        command = IntegerParser.parse(self, arg)
        TurtleDrawer.draw_line(self, 270, command)

    def do_square(self, arg):
        """Draw Square"""
        command = IntegerParser.parse(self, arg)
        directions = [0, 90, 180, 270]
        for i in directions:
            TurtleDrawer.draw_line(self, i, command)

    def do_circle(self,arg):
        """Draw Circle"""
        command = IntegerParser.parse(self, arg)
        TurtleDrawer.draw_circle(self,command)

    def do_Exit(self, arg):
        """Exit Turtle CMD"""
        print("Bye")
        return True
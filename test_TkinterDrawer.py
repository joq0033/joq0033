import unittest
from TkinterDrawer import TkinterDrawer
from Parser import ArgumentParser
from Parser import IntegerParser
from Parser import StringParser
from SourceReader import ArgumentSourceReader
from TurtleDrawer import TurtleDrawer

class TestTkinterDrawer(unittest.TestCase):

    def setUp(self):
        self.tkinterDrawer = TkinterDrawer()

    def test_select_pen(self):
        raised = False
        try:
            self.tkinterDrawer.select_pen(1)
        except:
            raised = True
        self.assertTrue(raised, "Error Raised")

    # def test_pen_down(self):
    #     self.tkinterDrawer.pen_down()
    #     self.assertTrue(self.tkinterDrawer.pen_state)

    def test_pen_down(self):
        raised = False
        try:
            self.tkinterDrawer.pen_down(250, 50)
        except:
            raised = True
        self.assertTrue(raised, "Error Raised")

    # def test_pen_up(self):
    #     self.tkinterDrawer.pen_up()
    #     self.assertFalse(self.tkinterDrawer.pen_state)

    def test_pen_up(self):
        raised = False
        try:
            self.tkinterDrawer.pen_down(50, 250)
        except:
            raised = True
        self.assertTrue(raised, "Error Raised")

    def test_go_along(self):
        raised = False
        try:
            self.tkinterDrawer.go_along(self.tkinterDrawer.x(50))
        except:
             raised = True
        self.assertTrue(raised, "Error Raised")

    def test_go_down(self):
        raised = False
        try:
            self.tkinterDrawer.go_down(self.tkinterDrawer.y(50))
        except:
            raised = True
        self.assertTrue(raised, "Error Raised")

    def test_draw_line(self):
        raised = False
        try:
            self.tkinterDrawer.draw_line(90)
        except:
            raised = True
        self.assertTrue(raised, "Error Raised")

    def test_draw_square(self):
        raised = False
        try:
            self.tkinterDrawer.draw_square(0, 90, 180, 270)
        except:
            raised = True
        self.assertTrue(raised, "Error Raised")

    def test_draw_circle(self):
        raised = False
        try:
            self.tkinterDrawer.draw_circle(250 - 50, 250 - 50, 250 + 50, 250 + 50,width=self.line_width)
        except:
            raised = True
        self.assertTrue(raised, "Error Raised")

    def test_draw_triangle(self):
        raised = False
        try:
            self.tkinterDrawer.draw_triangle(55, 85, 155, 85, 105, 180, 55, 85, width=self.line_width)
        except:
            raised = True
        self.assertTrue(raised, "Error Raised")

class TestArgumentSourceReader(unittest.TestCase):

    def setUp(self):
        self.tkinterReader = ArgumentSourceReader(ArgumentParser(TurtleDrawer()))
        self.source = ['-e', '-t', '-k', '-g']

    def test_go(self):
        raised = False
        try:
            self.tkinterReader.go(self.source)
        except:
            raised = True
        self.assertTrue(raised, "Error Raised")

class TestArgumentParser(unittest.TestCase):

    def setUp(self):
        self.tkinterParser = ArgumentParser(TurtleDrawer())
        # self.source = ['-c', '-e', '-t', '-k', '-g']

    def test_parse(self):
        raised = False
        try:
            self.tkinterParser.parse()
        except:
            raised = True
        self.assertTrue(raised, "Error Raised")


class TestIntegerParser(unittest.TestCase):
        def setUp(self):
            self.tkinterIntParser = IntegerParser(TurtleDrawer())
            self.source = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        def test_parse(self):
            raised = False
            try:
                self.tkinterIntParser.parse(self.source)
            except:
                raised = True
            self.assertTrue(raised, "Error Raised")

class TestStringParser(unittest.TestCase):

        def setUp(self):
            self.tkinterStrParser = StringParser(TurtleDrawer())
            # self.source = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '']

        def test_parse(self):
            raised = False
            try:
                self.tkinterStrParser.parse()
            except:
                raised = True
            self.assertTrue(raised, "Error Raised")

if __name__ == '__main__':
    unittest.main()


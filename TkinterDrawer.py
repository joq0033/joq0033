from TIGr import AbstractDrawer
from Parser import IntegerParser, StringParser
from tkinter import *
from tkinter import ttk
import math
#Alliah & Chris

class TkinterDrawer(AbstractDrawer):
    def __init__(self):
        self.root = Tk()
        self.north = Entry(self.root)
        self.direction = 0
        self.distance = 0
        self.pen_button = Button()
        self.color_button = Button()
        self.eraser_button = Button()
        self.north_button = Button()
        self.south_button = Button()
        self.west_button = Button()
        self.east_button = Button()
        self.square_button = Button()
        self.circle_button = Button()
        self.triangle_button = Button()
        self.up = Button()
        self.down = Button()
        self.clear_canvas = Button()
        self.choose_size_button = Scale()
        self.c = Canvas()
        self.x = 0
        self.y = 0
        self.entry = 0.0
        self.line_width = 1
        self.button = Button()
        self.north = Entry()
        self.entry = self.north.get()
        self.line_width = self.choose_size_button.get()
        self.pen_state = True

    def setup(self):

        self.root.geometry("510x645")
        self.choose_size_button = 1
        self.x = 250
        self.y = 250
        self.color = "black"

        self.c = Canvas(self.root, bg='white', width=500, height=500)
        self.c.grid_rowconfigure(0, weight=1)
        self.c.grid_columnconfigure(0, weight=1)

        pen_size = Label(self.root, text="Pen Size: ")
        pen_size.grid(row=1, column=4, pady=12)
        self.choose_size_button = Scale(self.root, from_=1, to=2, orient=HORIZONTAL)
        self.choose_size_button.grid(row=1, column=5)

        self.north_button = Button(self.root, text=' → ', command=lambda: self.draw_line(0, 50))
        self.north_button.grid(row=1, column=2, sticky=W,padx = 10)

        self.south_button = Button(self.root, text=' ← ', command=lambda: self.draw_line(180, 50))
        self.south_button.grid(row=1, column=0, sticky=E,padx = 10)

        self.east_button = Button(self.root, text='  ↑  ', command=lambda: self.draw_line(90, 50))
        self.east_button.grid(row=0, column=1, sticky=SW)

        self.west_button = Button(self.root, text='  ↓  ', command=lambda: self.draw_line(270, 50))
        self.west_button.grid(row=2, column=1, sticky=NW)

        separator = ttk.Separator(self.root, orient=VERTICAL)
        separator.grid(row=1, column=3, sticky=NS)

        self.up = Button(self.root, text='Pen up', command=lambda: self.pen_up())
        self.up.grid(row=0, column=4, pady=10)

        self.down = Button(self.root, text='Pen down', command=lambda: self.pen_down())
        self.down.grid(row=0, column=5, pady=10)

        self.clear_canvas = Button(self.root, text='Clear Canvas', command=lambda: self.reset())
        self.clear_canvas.grid(row=0, column=6, pady=10)

        self.square_button = Button(self.root, text='square', command=lambda: self.draw_square())
        self.square_button.grid(row=2, column=4, pady=10)
        self.circle_button = Button(self.root, text='circle', command=lambda: self.draw_circle())
        self.circle_button.grid(row=2, column=5)
        self.triangle_button = Button(self.root, text='triangle', command=lambda: self.draw_triangle())
        self.triangle_button.grid(row=2, column=6, pady=10)
        self.c.grid(row=60, columnspan=60)
        self.line_width = self.choose_size_button.get()
        self.c.bind('<B1-Motion>', self.draw_line)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def select_pen(self, pen_num):
        self.activate_button(self.pen_button)
        self.line_width = self.choose_size_button.get()

    def pen_down(self):
        self.pen_state = True

    def pen_up(self):
        self.pen_state = False

    def go_along(self, along):
        self.x = along

    def go_down(self, down):
        self.y = down

    def draw_line(self, direction, distance):
        if not self.pen_state:
            self.color = "white"
        else:
            self.color = "black"

        if direction == 0:
            new_direction = 0

        if direction == 180:
            new_direction = 180
        if direction == 90:
            new_direction = 270
        if direction == 270:
            new_direction = 90

        angle_in_radians = new_direction * math.pi / 180

        line_length = distance
        center_x = self.x
        center_y = self.y

        end_x = center_x + line_length * math.cos(angle_in_radians)
        end_y = center_y + line_length * math.sin(angle_in_radians)
        self.line_width = self.choose_size_button.get()
        self.c.create_line(self.x, self.y, end_x, end_y, fill=self.color, width=self.line_width)
        self.x = end_x
        self.y = end_y

    def draw_square(self):
        if self.pen_state:
            directions = [0, 90, 180, 270]
            for i in directions:
                self.draw_line(i, 50)

    def draw_circle(self):
        r = 50
        if self.pen_state:
            self.c.create_oval(self.x - r, self.y - r, self.x + r, self.y + r,width=self.line_width)

    def draw_triangle(self):
        self.c.create_line(55, 85, 155, 85, 105, 180, 55, 85, width=self.line_width)

    # def reset(self):
    #     self.x = 250
    #     self.y = 250
    #     self.c.delete("all")
    #
    # def start(self):
    #     self.setup()
    #     self.root.mainloop()

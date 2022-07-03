from turtle import Screen
WIDTH = 600
HEIGHT = 600
TITLE = "Snake Game"
BG_COLOR = "black"


class Utility:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=WIDTH, height=HEIGHT)
        self.screen.bgcolor(BG_COLOR)
        self.screen.title(TITLE)
        self.screen.tracer(0)

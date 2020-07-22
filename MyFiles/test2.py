from manimlib.imports import *


class CircleExample(Scene):
    def construct(self):
        c = Circle()
        self.play(ShowCreation(c))

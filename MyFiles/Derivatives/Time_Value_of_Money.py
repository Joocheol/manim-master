from manimlib.imports import *


class a_01(Scene):
    def construct(self):
        a = Line()
        self.play(ShowCreation(a))
        self.wait()
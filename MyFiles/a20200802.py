from manimlib.imports import *

class a20200802(Scene):
    def construct(self):
        rect = Rectangle(height=0.5, width=0.5)
        rect.set_fill(YELLOW, opacity=0.8)
        rect.set_stroke(width=0)

        group = VGroup(*[rect.copy() for i in range(5)])
        group.arrange(RIGHT)
        group_1 = VGroup(*[group.copy() for i in range(3)])
        group_1.arrange(DOWN)

        self.play(Write(group_1))
        self.wait(2)


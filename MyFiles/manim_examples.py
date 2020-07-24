from manimlib.imports import *

class manim_examples(Scene):
    def construct(self):

        c = Circle()
        d = Dot()

        g = VGroup(c, d)

        self.add(g)
        self.play(g.move_to, RIGHT*5, run_time=3)
        self.wait()
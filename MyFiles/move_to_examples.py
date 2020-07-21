from manimlib.imports import *


class move_to_ex01(Scene):
    def construct(self):
        locations = [UP, DOWN, LEFT, RIGHT, ORIGIN]
        c = Dot()
        self.add(c)
        self.wait()

        for loc in locations:
            for i in range(1,5):
                self.play(c.move_to, i*loc)
                self.wait()
from manimlib.imports import *


class move_to_ex01(Scene):
    def construct(self):

        for x in range(-7, 7):
            for y in [3, 2, -2, 0]:
                c = Dot()
                self.add(c)
                c.move_to(np.array([x, y, 0]))
                self.play(Write(c))

#                self.play(c.move_to, np.array([x, y, 0]))

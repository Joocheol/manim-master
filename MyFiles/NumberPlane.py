from manimlib.imports import *

class NumberPlane_example(Scene):
    def construct(self):

        plane = NumberPlane()
        v_1 = Vector(direction=[1, 2], color='YELLOW')
        self.play(ShowCreation(plane))
        self.add(v_1)
        self.wait()
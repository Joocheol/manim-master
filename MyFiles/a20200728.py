from manimlib.imports import *


class WhatIsAVectorInFinance(Scene):
    def construct(self):

        self.intro_vector()

    def intro_vector(self):
        plane = NumberPlane()
        # labels = VMobject(*plane.get_coordinate_labels())
        # labels = VMobject(plane)
        labels = TextMobject("label")
        vector = Vector([5, 1], color=YELLOW)
        coordinates = Matrix([5, 1])
        symbol = TexMobject("\\vec{\\textbf{v}}")
        symbol.shift(0.5 * (RIGHT + UP))

        self.play(ShowCreation(
            plane,
            lag_ratio=1,
            run_time=3
        ))
        self.play(ShowCreation(
            vector,
        ))
        self.play(
            Write(labels),
            Write(coordinates),
            Write(symbol)
        )
        self.wait(2)
        self.play(
            FadeOut(plane),
            FadeOut(labels),
            ApplyMethod(vector.shift, 4 * LEFT + UP),
            ApplyMethod(coordinates.shift, 2.5 * RIGHT + 0.5 * DOWN),
            ApplyMethod(symbol.shift, 0.5 * (UP + LEFT))
        )
        self.remove(plane, labels)
        return vector, symbol, coordinates


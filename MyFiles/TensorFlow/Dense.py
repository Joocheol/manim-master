from manimlib.imports import *


class Dense(Scene):
    def construct(self):

        # text_01 = TextMobject(
        #     r"\begin{verbatim}tf.keras.layers.Dense()\end{verbatim}"
        # ).scale(1.5)
        # self.play(Write(text_01))

        mat_1 = Matrix([[1, 2], [3, 4]])

        self.play(Write(mat_1))
        self.wait()
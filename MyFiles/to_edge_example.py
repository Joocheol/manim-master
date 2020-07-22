from manimlib.imports import *


class to_edge_example(Scene):
    def construct(self):
        text = TexMobject(r"\int x \, dx")

        self.play(text.to_edge, np.array([-1, -10, 0]))
        self.wait()

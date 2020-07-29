from manimlib.imports import *


class BrownianMotion(GraphScene):
    def construct(self):
        self.setup_axes(animate=False)
        self.simple_func()
        self.wait()

        print(np.linspace(0, 1))

    def simple_func(self):
        graph = FunctionGraph(
            lambda x: x + np.random.normal(),
            x_min=0,
            x_max=5,
            color=YELLOW,
            stroke_width=1,
        )
        self.play(ShowCreation(graph))
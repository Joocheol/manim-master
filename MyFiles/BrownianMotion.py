from manimlib.imports import *


class BrownianMotion(GraphScene):
    def construct(self):
        self.setup_axes(animate=False)
        self.not_simple_func(seed=999)
        self.wait()

        print(np.linspace(0, 1))

    def my_function(self, x):
        x = np.sqrt(np.random.normal())
        return x

    def not_simple_func(self, seed=1):
        np.random.seed(seed)
        graph = FunctionGraph(

            lambda x: np.exp(x * self.my_function(x)),
            x_min=0
        )
        self.play(ShowCreation(graph))
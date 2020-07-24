from manimlib.imports import *


class Start(GraphScene):
    CONFIG = {
        "x_min": -10,
        "x_max": 10,
        "x_axis_width": 10,
        "x_tick_frequency": 1,
        "x_leftmost_tick": None,  # Change if different from x_min
        "x_labeled_nums": None,
        "x_axis_label": "$x$",
        "y_min": -7,
        "y_max": 7,
        "y_axis_height": 7,
        "y_tick_frequency": 1,
        "y_bottom_tick": None,  # Change if different from y_min
        "y_labeled_nums": None,
        "y_axis_label": "$y$",
        "axes_color": GREY,
        "graph_origin": ORIGIN,
        "exclude_zero_label": True,
        "default_graph_colors": [BLUE, GREEN, YELLOW],
        "default_derivative_color": GREEN,
        "default_input_color": YELLOW,
        "default_riemann_start_color": BLUE,
        "default_riemann_end_color": GREEN,
        "area_opacity": 0.8,
        "num_rects": 50,
    }

    def construct(self):
        self.setup_axes()

        graph_1 = FunctionGraph(
            lambda x: 3/x,
            x_min=0.86,
            x_max=5
        )
        graph_2 = FunctionGraph(
            lambda x: 3 / x,
            x_min=-5,
            x_max=-0.86
        )

        self.play(
            ShowCreation(graph_1),
            ShowCreation(graph_2),
        )

        c = Circle(radius=1)

        self.play(ShowCreation(c))


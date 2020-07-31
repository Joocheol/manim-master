from manimlib.imports import *


class a2020073105(Scene):
    def construct(self):
        text_01 = TextMobject(
            r'''$n$ linear equations, $n$ unknowns'''
        )

        text_02 = TextMobject(
            r'''Row picture'''
        )
        text_02.next_to(text_01, DOWN)

        text_03 = TextMobject(
            r'''(*) Column picture'''
        )
        text_03.next_to(text_02, DOWN)

        text_04 = TextMobject(
            r'''Matrix form'''
        )
        text_04.next_to(text_03, DOWN)

        vg_1 = VGroup(text_01, text_02, text_03, text_04)
        vg_1.move_to(ORIGIN)

        self.play(Write(vg_1))


class a2020073106(Scene):
    def construct(self):
        formula_1 = TexMobject(r'''
            2x  - y = 0 \\
            -x  + 2y = 3
        ''')

        self.play(Write(formula_1))

        self.play(formula_1[0][12].move_to, TOP)


class a2020073111(GraphScene):
    CONFIG = {
        "x_min": -FRAME_X_RADIUS,
        "x_max": FRAME_X_RADIUS,
        "x_axis_width": FRAME_WIDTH,
        "x_leftmost_tick": int(-FRAME_X_RADIUS),
        "y_min": -FRAME_Y_RADIUS,
        "y_max": FRAME_Y_RADIUS,
        "y_axis_height": FRAME_HEIGHT,
        "graph_origin": ORIGIN,
    }

    def construct(self):
        formula_1 = TexMobject(r'''
                    2x  - y = 0 \\
                    -x  + 2y = 3
                ''')

        formula_1.to_corner(UL, buff=LARGE_BUFF)
        self.add(formula_1)

        self.setup_axes()

        g_1 = self.get_graph(
            lambda x: 2 * x,
            color=YELLOW)

        g_2 = self.get_graph(
            lambda x: (1/2) * x + (3/2),
            color=BLUE)

        self.play(ShowCreation(g_1), formula_1[0][0:6].set_color, YELLOW)
        self.wait()

        self.play(ShowCreation(g_2), formula_1[0][6:14].set_color, BLUE)
        self.wait()

        dot = Dot().move_to(self.coords_to_point(1, 2)).set_color(WHITE)
        line_1 = DashedLine(self.coords_to_point(1, 2), self.coords_to_point(1, 0))
        line_2 = DashedLine(self.coords_to_point(1, 2), self.coords_to_point(0, 2))
        num_1 = TexMobject("1")
        num_2 = TexMobject("2")
        num_1.next_to(line_1, DOWN)
        num_2.next_to(line_2, LEFT)
        self.add(dot)
        self.play(ShowCreation(line_1), ShowCreation(line_2))
        self.play(Write(num_1), Write(num_2))
        self.wait()

class a2020073112(GraphScene):
    CONFIG = {
        "x_min": -FRAME_X_RADIUS,
        "x_max": FRAME_X_RADIUS,
        "x_axis_width": FRAME_WIDTH,
        "x_leftmost_tick": int(-FRAME_X_RADIUS),
        "y_min": -FRAME_Y_RADIUS,
        "y_max": FRAME_Y_RADIUS,
        "y_axis_height": FRAME_HEIGHT,
        "graph_origin": ORIGIN,
    }
    def construct(self):
        formula_1 = TexMobject(r'''
                            2x  - y = 0 \\
                            -x  + 2y = 3
                        ''')

        formula_1.to_corner(UL, buff=LARGE_BUFF)
        self.add(formula_1)

        formula_2 = TexMobject(r'''
        x \begin{bmatrix} 2 \\ -1 \end{bmatrix}
        + y \begin{bmatrix} -1 \\ 2 \end{bmatrix}
        = \begin{bmatrix} 0 \\ 3 \end{bmatrix}
        ''')

        self.add(formula_2[0][5])
        self.wait()

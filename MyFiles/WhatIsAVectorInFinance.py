from manimlib.imports import *


class Scene_01(Scene):
    def construct(self):
        # self.title()
        # self.coin_tossing(["H", "T"], run_time=2)
        # self.coin_tossing(["HEAD", "TAIL"], run_time=2)
        # self.coin_tossing(["UP", "DOWN"], run_time=2)
        self.bernoulli()
        # self.intro_vector()

    def bernoulli(self):
        formula = TexMobject(r'''
            \textrm{Payoff} = \left.
            \begin{cases}
            22 \quad \textrm{if head} \\
            1
            \end{cases}
        ''')

        self.play(Write(formula))
        return self

    def coin_tossing(self, s, **kwargs):
        c_1 = Circle()
        s_1 = TextMobject(s[0])
        v_1 = VGroup(c_1, s_1)

        c_2 = Circle()
        s_2 = TextMobject(s[1])
        v_2 = VGroup(c_2, s_2)
        v_2.rotate(TAU / 4, UP)

        # v_3 = VGroup(v_1, v_2).arrange()
        self.play(v_1.rotate, TAU / 4, UP, **kwargs)
        self.remove(v_1)
        self.play(v_2.rotate, -TAU / 4, UP, **kwargs)
        self.wait(0.5)
        self.remove(v_2)
        return self

    def title(self):
        top = TextMobject("What is a vector in finance?")

        self.play(Write(top))
        self.wait()
        self.play(FadeOut(top))

        return self

    def intro_vector(self):
        plane = NumberPlane()

        label_x = TextMobject("UP")
        label_x.move_to(6 * RIGHT + 0.5 * DOWN)
        label_y = TextMobject("DOWN")
        label_y.move_to(3.5 * UP + LEFT)

        vector = Vector([5, 1], color=YELLOW)
        coordinates = Matrix([5, 1])
        symbol = TexMobject("\\vec{\\textbf{v}}")
        symbol.shift(0.5 * (RIGHT + UP))

        self.play(ShowCreation(
            plane,
            lag_ratio=1,
            run_time=3
        ))

        self.play(
            Write(label_x),
            Write(label_y),
            # Write(coordinates),
            # Write(symbol)
        )

        self.play(ShowCreation(
            vector,
        ))
        self.wait(2)
        # self.play(
        #     FadeOut(plane),
        #     FadeOut(label_x),
        #     FadeOut(label_y),
        #     ApplyMethod(vector.shift, 4 * LEFT + UP),
        #     ApplyMethod(coordinates.shift, 2.5 * RIGHT + 0.5 * DOWN),
        #     ApplyMethod(symbol.shift, 0.5 * (UP + LEFT))
        # )
        self.remove(plane, label_x, label_y)
        return vector, symbol, coordinates

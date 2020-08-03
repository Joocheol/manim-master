from manimlib.imports import *


class b2020080321(Scene):
    def construct(self):
        t_1 = TextMobject(r"For another vector $\bold{w} = (w_{1}, w_{2}, \cdots, w_{m})$,")
        t_1.to_edge(UL, buff=1)
        self.play(Write(t_1))

        f_1 = TexMobject(r"\bra{\bold{w}} = [ \bar{w}_{1}, \bar{w}_{2}, \cdots, \bar{w}_{m} ]")
        f_1.next_to(t_1, DOWN)
        self.play(Write(f_1))

        f_2 = TexMobject(r"\ket{\bold{w}} = \begin{bmatrix} w_{1} \\ w_{2} \\ \vdots \\ w_{m} \end{bmatrix}")
        f_2.next_to(f_1, DOWN)
        self.play(Write(f_2))

        # f_3 = TexMobject(r"\ket{\bold{v}} \bra{\bold{w}}")
        # f_3.next_to(f_2)
        # self.play(Write(f_3))


class b2020080320(Scene):
    def construct(self):
        t_1 = TextMobject(r"Given a vector $\bold{v} = (v_{1}, v_{2}, \cdots, v_{n})$,")
        t_1.to_edge(UL, buff=1)
        self.play(Write(t_1))

        f_1 = TexMobject(r"\bra{\bold{v}} = [ \bar{v}_{1}, \bar{v}_{2}, \cdots, \bar{v}_{n} ]")
        f_1.next_to(t_1, DOWN)
        self.play(Write(f_1))

        f_2 = TexMobject(r"\ket{\bold{v}} = \begin{bmatrix} v_{1} \\ v_{2} \\ \vdots \\ v_{n} \end{bmatrix")
        f_2.next_to(f_1, DOWN)
        self.play(Write(f_2))

        g_all = VGroup(t_1, f_1, f_2)

        self.play(FadeOut(g_all))


class b2020080319(Scene):
    def construct(self):
        t_1 = TextMobject("Bras and Kets")
        t_1.scale(3)

        self.play(Write(t_1))
        self.wait(2)
        self.play(FadeOut(t_1))

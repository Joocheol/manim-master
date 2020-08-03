from manimlib.imports import *


class a2020080406(Scene):
    def construct(self):
        t_1 = TextMobject(r"\textbf{Example}")
        t_1.to_edge(UP)

        self.play(Write(t_1))
        self.wait()

        v_1 = TexMobject(r"\bold{v} &= (3, -i) \\ \bold{w} &= (2+i, 4)")
        v_2 = TexMobject(
            r"""\bra{v} &= \begin{bmatrix} 3 & i \end{bmatrix} \\ 
            \ket{w} &= \begin{bmatrix} 2+i \\ 4 \end{bmatrix}"""
        )
        g_1 = VGroup(v_1, v_2).arrange(4*RIGHT).move_to(2*UP)

        self.play(Write(g_1))
        self.wait()

        v_3 = TexMobject(
            r"\braket{v}{w} = 3 ( 2 + i ) + 4i = 6 + 7i"
        )
        v_3.next_to(g_1, 2*DOWN)

        self.play(Write(v_3))
        self.wait()

        v_4 = TexMobject(
            r"""\ket{w}\bra{v}  
            = \begin{bmatrix} (2+i) 3 & (2+i) i \\ 4\cdot 3 & 4i \end{bmatrix}
            = \begin{bmatrix} 6+3i & 2i - 1 \\ 12 & 4i \end{bmatrix}
            """
        )
        v_4.next_to(v_3, 2 * DOWN)

        self.play(Write(v_4))
        self.wait()


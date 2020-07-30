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
            2x  - y &= 0 \\
            -x  +2y &= 3
        ''')

        self.play(Write(formula_1))

        self.play(formula_1[0][12].move_to, TOP)
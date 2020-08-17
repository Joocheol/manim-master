from manimlib.imports import *


class intro(Scene):
    def construct(self):
        title = TextMobject("Credit Business").scale(2)
        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))

        text_01 = TextMobject("Present").move_to(LEFT * 3 + UP * 3)
        text_02 = TextMobject("Future").move_to(RIGHT * 3 + UP * 3)
        formula_01 = TexMobject(r"\$ 10").move_to(LEFT * 3 + UP * 1)
        formula_02 = TexMobject(r"\$ 11").move_to(RIGHT * 3 + UP * 1)
        formula_03 = TexMobject(r"S_0").move_to(LEFT * 3 + UP * -2)
        formula_04 = TexMobject(r"S_T").move_to(RIGHT * 3 + UP * -2)
        line_01 = DashedLine(start=TOP, end=BOTTOM)
        # line_02 = Line(start=LEFT*2.5, end=RIGHT*2.5).move_to([0, 1, 0])
        # line_03 = Line(start=LEFT * 2.5, end=RIGHT * 2.5).move_to([0, -1, 0])
        arrow_01 = DoubleArrow(formula_03.get_top(), formula_01.get_bottom())
        arrow_02 = DoubleArrow(formula_03.get_top(), formula_02.get_bottom())
        arrow_03 = DoubleArrow(formula_04.get_top(), formula_01.get_bottom())
        arrow_04 = DoubleArrow(formula_04.get_top(), formula_02.get_bottom())

        self.add(text_01)
        self.add(text_02)
        self.add(line_01)

        self.play(
            Write(formula_01),
            Write(formula_02),
            Write(formula_03),
        )
        self.wait()

        self.play(
            ShowCreation(arrow_02),
        )
        self.wait()



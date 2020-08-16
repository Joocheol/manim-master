from manimlib.imports import *

class intro(Scene):
    def construct(self):
        self.wait()

class intro_02(Scene):
    def construct(self):
        game1 = TexMobject("10")
        game1.scale(1).move_to(RIGHT * -4.75 + UP * 0)
        game1_up = TexMobject("11")
        game1_up.scale(1).move_to(RIGHT * -3.25 + UP * 1)
        game1_down = TexMobject("11")
        game1_down.scale(1).move_to(RIGHT * -3.25 + UP * -1)

        game2 = TexMobject("9")
        game2.scale(1).move_to(RIGHT * -1.0 + UP * 0)
        game2_up = TexMobject("22")
        game2_up.scale(1).move_to(RIGHT * 0.5 + UP * 1)
        game2_down = TexMobject("0")
        game2_down.scale(1).move_to(RIGHT * 0.5 + UP * -1)

        game3 = TexMobject("?")
        game3.scale(1).move_to(RIGHT * 3.0 + UP * 0)
        game3_up = TexMobject("22")
        game3_up.scale(1).move_to(RIGHT * 4.7 + UP * 1)
        game3_down = TexMobject("11")
        game3_down.scale(1).move_to(RIGHT * 4.7 + UP * -1)

        line_01 = DashedLine(start=UP, end=DOWN).move_to([-2.0, 0, 0])
        line_02 = DashedLine(start=UP, end=DOWN).move_to([2.0, 0, 0])

        self.play(
            Write(game1), Write(game1_up), Write(game1_down),

            # Write(game3), Write(game3_up), Write(game3_down)
        )
        self.wait(1)

        self.play(
            ShowCreation(line_01)
        )

        self.play(
            Write(game2), Write(game2_up), Write(game2_down),
        )
        self.wait()

        self.play(
            ShowCreation(line_02)
        )
        self.wait()

        self.play(
            Write(game3), Write(game3_up), Write(game3_down)
        )

class intro_01(Scene):
    def construct(self):
        game1 = TexMobject("10")
        game1_up = TexMobject("11")
        game1_down = TexMobject("11")
        g_1 = VGroup(game1_up, game1_down).arrange(DOWN*2)
        line_01 = Line(start=DOWN, end=UP)
        line_02 = Line(start=LEFT * 3.5, end=RIGHT * 3.5)
        text_01 = TextMobject(r"Present")
        text_02 = TextMobject(r"Future")

        self.add(line_01)
        self.add(text_01.move_to(LEFT * 4 + UP * 3))
        self.add(text_02.move_to(RIGHT * 4 + UP * 3))
        self.add(game1.move_to(LEFT * 4))
        self.add(game1_up.move_to(RIGHT * 4))
        self.add(game1_down.move_to(RIGHT * 4))
        self.wait()

        self.play(
            Transform(line_01, line_02),
        )
        self.wait()

        self.play(
            game1_up.shift, UP,
            game1_down.shift, DOWN,
            FadeOut(line_01),
        )
        self.wait()



from manimlib.imports import *
import MyFiles.MyLib.MyModules as My

class a2020080209(Scene):
    def construct(self):
        rect = Rectangle(height=0.25, width=0.25).set_fill(YELLOW, opacity=0.8).set_stroke(width=0)

        a = My.add_brackets(rect)

        self.play(Write(a))
        self.wait()

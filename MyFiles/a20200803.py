from manimlib.imports import *
import MyFiles.MyLib.MyModules as My

class a20200803(Scene):
    def construct(self):
        text = r"""
from manimlib.imports import *

# computer code printing
def code(text):

    run_time = len(text) / 30
    tmp = TextMobject("\\begin{erbatim} " + text + "\\end{erbatim}").set_color(GRAY)
    self.play(ShowCreation(tmp.scale(0.6).to_edge(UL, buff=1)), run_time=run_time)
"""
        My.code(self, text)

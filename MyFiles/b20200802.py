from manimlib.imports import *


class b20200802(Scene):
    def construct(self):
        text = """
from manimlib.scene.scene import Scene   
from manimlib.utils.sounds import play_error_sound
from manimlib.utils.sounds import play_finish_sound
import manimlib.constants


def open_file_if_needed(file_writer, **config):
    if config["quiet"]:
        curr_stdout = sys.stdout
        sys.stdout = open(os.devnull, "w")
        """
        time = len(text)/30

        tmp = TextMobject("\\begin{verbatim} " + text + "\\end{verbatim}").set_color(GRAY)

        self.play(ShowCreation(tmp.scale(0.6).to_edge(UL, buff=1)), run_time=time, rate_function=linear)

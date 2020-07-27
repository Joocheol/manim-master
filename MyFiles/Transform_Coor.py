from manimlib.imports import *

EXAMPLE_TRANFORM = [[0, 1], [-1, 1]]
TRANFORMED_VECTOR = [[2], [3]]

class ExampleTransformation(LinearTransformationScene):
    def construct(self):
        self.setup()
        self.add_vector(np.array(TRANFORMED_VECTOR).flatten())
        self.apply_matrix(EXAMPLE_TRANFORM)
        self.wait()
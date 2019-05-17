import numpy as np
class Velocity():
    def __init__(self, x=0,y=0,max=40):
        self.value = np.array([x,y],dtype=float)
        self.max = max

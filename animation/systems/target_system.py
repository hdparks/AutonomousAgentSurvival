import numpy as np
import pygame
class TargetSystem():
    def __init__(self, manager):
        self.manager = manager
        manager.archetypes[('vel','pos','target')] = 'targetSystem'
        manager.collections['targetSystem'] = []

    def execute(self):
        dt = self.manager.clock.get_time()/1000
        for i in self.manager.collections['targetSystem']:
            vel = i.get('vel')
            pos = i.get('pos')
            target = i.get('target')

            vec = target.value - pos.value


            vecnorm = np.linalg.norm(vec)

            # vec is less-than or equal to 10
            if vecnorm > 50:
                vec = vec * 50 / vecnorm

            vel.value = vec

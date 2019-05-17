import numpy as np

class VelocityDampingSystem():
    def __init__(self,manager):
        self.manager = manager
        manager.archetypes[('vel',)] = 'velocityDampingSystem'
        manager.collections['velocityDampingSystem'] = []

    def execute(self):

        for i in self.manager.collections['velocityDampingSystem']:
            vel = i.get('vel')

            norm = np.linalg.norm(vel.value)

            if norm > vel.max:
                vel.value *= vel.max / norm

import math

class MovementSystem():
    def __init__(self, manager):
        self.manager = manager

        manager.archetypes[('pos','vel')] = 'movers'
        manager.collections['movers'] = []

    def execute(self):
        dt = self.manager.clock.get_time()/1000
        for i in self.manager.collections['movers']:
            pos = i.get('pos')
            vel = i.get('vel')

            pos.value += vel.value * dt

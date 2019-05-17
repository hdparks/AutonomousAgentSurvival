class WellAnimationSystem():
    """ Handles animating well sprites """
    def __init__(self, manager):
        self.manager = manager
        manager.archetypes[('spritesheet','wellActive')] = 'wellActive'
        manager.collections['wellActive'] = []

    def execute(self):
        for i in self.manager.collections['wellActive']:
            s = i.get('spritesheet')
            active = i.get('wellActive')

            if active.active:
                active.cooldown -=1

            if active.cooldown <= 0:
                s.cellIndex = (s.cellIndex + 1) % s.totalCellCount
                active.cooldown = active.frameDelay

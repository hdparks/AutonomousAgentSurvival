class AgentAnimationSystem():
    """ Handles animating active agents """
    def __init__(self, manager):
        self.manager = manager
        manager.archetypes[('spritesheet','agentActive')] = 'agentActive'
        manager.collections['agentActive'] = []

    def execute(self):
        for i in self.manager.collections.get('agentActive'):
            s = i.get('spritesheet')
            active = i.get('agentActive')

            if active.active:
                active.cooldown -= 1

            if active.cooldown <= 0:
                s.cellIndex = (s.cellIndex + 1) % s.totalCellCount
                active.cooldown = active.frameDelay


class RenderSystem():
    """ Handles rendering spritesheets """
    def __init__(self,manager):
        self.manager = manager
        manager.archetypes[('spritesheet','pos')] = 'renderables'
        manager.collections['renderables'] = []


    def execute(self):
        for i in self.manager.collections['renderables']:
            s = i.get('spritesheet')
            pos = i.get('pos')
            s.surface.blit(
                s.sheet,
                (pos.value[0], pos.value[1]),
                s.cells[s.cellIndex]
            )

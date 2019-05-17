import pygame
class RenderTrackingSystem():
    def __init__(self,manager,surface):
        self.manager = manager
        self.surface = surface

    def execute(self):
        for i in self.manager.collections.get('targetSystem'):
            target = i.get('target')
            pygame.draw.circle(self.surface,(250,0,0),target.value.astype(int),25)

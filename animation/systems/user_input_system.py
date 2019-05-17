import pygame
from ..components.spacebar_press import SpacebarPress

class InputSystem():
    """ Handles user Input """
    def __init__(self, manager):
        self.manager = manager
        manager.archetypes[('spacebar',)] = 'spacebar'
        manager.collections['spacebar'] = []

    def execute(self):

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            # Only add if not already one in the queue
            if len(self.manager.collections['spacebar']) == 0:

                entity = { 'spacebar' : SpacebarPress() }
                self.manager.create_entity(entity)

class InputCooldownSystem():
    def __init__(self, manager):
        self.manager = manager

    def execute(self):
        if len(self.manager.collections['spacebar']) > 0:
            entity = self.manager.collections['spacebar'][0]
            spacebar = entity.get('spacebar')
            spacebar.cooldown -= 1
            if spacebar.cooldown <= 0:
                self.manager.mark_for_deletion(entity)

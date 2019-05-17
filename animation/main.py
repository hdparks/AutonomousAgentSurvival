from World import World
import pygame, sys
from pygame.locals import *
from .systems.user_input_system import InputSystem, InputCooldownSystem
from .systems.render_system import RenderSystem
from .systems.well_animation_system import WellAnimationSystem
from .systems.agent_animation_system import AgentAnimationSystem
from .systems.velocity_damping_system import VelocityDampingSystem
from .systems.movement_system import MovementSystem
from .systems.target_system import TargetSystem
from .systems.world_act_system import WorldActSystem
from .systems.render_tracking_system import RenderTrackingSystem
from .manager import Manager
from .components.spritesheet import SpriteSheet
from .components.agent_active import AgentActive
from .components.well_active import WellActive
from .components.target import Target
from .components.position import Position
from .components.velocity import Velocity
import json

import random

## DEFAULT CONFIGURATION OBJECT
COLORS = {
    'BLACK' : (0,0,0),
    'WHITE' : (255,255,255),
    'RED' : (255,0,0),
    'GREEN' : (0,255,0),
    'BLUE' : (0,0,255)
    }

def events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def main(config_filename):
    pygame.init()
    CLOCK = pygame.time.Clock()
    CONFIG = { 'W':900, 'H':600, 'caption':"Default",'FPS':60 }
    DS = pygame.display.set_mode((CONFIG.get('W'),CONFIG.get('H')))
    pygame.display.set_caption(CONFIG.get('caption'))

    ## CREATE GAME SYSTEM INSTANCES HERE
    manager = Manager(CLOCK)
    render_system = RenderSystem(manager)
    well_animation_system = WellAnimationSystem(manager)
    agent_animation_system = AgentAnimationSystem(manager)
    input_system = InputSystem(manager)
    input_cooldown_system = InputCooldownSystem(manager)
    velocity_damping_system = VelocityDampingSystem(manager)
    movement_system = MovementSystem(manager)
    target_system = TargetSystem(manager)
    world_act_system = WorldActSystem(manager)


    ## LOAD IN ENTITIES HERE
    manager.world = World([1,0,0])
    manager.agent_map = []
    manager.config = CONFIG
    manager.DS = DS
    for agent in manager.world.agent_list:
        entity = {
            'pos':Position(
                agent.location[0] * CONFIG.get('W'),
                agent.location[1] * CONFIG.get('H')
                ),
            'vel':Velocity(),
            'spritesheet':SpriteSheet("animation/assets/StickFigure.png",4,1,DS),
            'agentActive':AgentActive(frameDelay = random.randint(7,13))
        }
        manager.create_entity(entity)
        manager.agent_map.append(entity)

    manager.well_map = []
    for well in [manager.world.wellA,manager.world.wellB,manager.world.wellC]:
        entity = {
            'pos':Position(well[0]*CONFIG.get('W'),well[1] * CONFIG.get("H")),
            'spritesheet':SpriteSheet("animation/assets/Well.png",4,2,DS),
            'wellActive':WellActive(active = False),
        }
        manager.create_entity(entity)
        manager.well_map.append(entity)

    while True:
        ## LOOP THROUGH GAME SYSTEMS HERE
        DS.fill(COLORS.get('BLACK'))
        input_system.execute()
        input_cooldown_system.execute()
        well_animation_system.execute()
        agent_animation_system.execute()
        target_system.execute()
        # velocity_damping_system.execute()
        movement_system.execute()
        render_system.execute()
        world_act_system.execute()
        manager.garbage_collection()
        manager.create_entities()


        events()
        pygame.display.update()
        CLOCK.tick(CONFIG.get('FPS'))








if __name__ == '__main__':
    config_filename = None if len(sys.argv) < 2 else sys.argv[1]
    main(config_filename)

from ..components.spritesheet import SpriteSheet
from ..components.agent_active import AgentActive
from ..components.target import Target
from ..components.position import Position
from ..components.velocity import Velocity
import random
class WorldActSystem():
    def __init__(self,manager):
        self.manager = manager
        self.reset = False

    def execute(self):
        # call act, storing agent index and choice
        for i in self.manager.collections.get('spacebar'):

            spacebar_press = i.get('spacebar')

            if spacebar_press.handled:
                break

            spacebar_press.handled = True

            if self.reset:

                # Delete all agent entities
                for entity in self.manager.agent_map:
                    self.manager.mark_for_deletion(entity)

                self.manager.agent_map = []
                for agent in self.manager.world.agent_list:
                    entity = {
                        'pos':Position(
                            agent.location[0] * self.manager.config.get('W'),
                            agent.location[1] * self.manager.config.get('H')
                            ),
                        'vel':Velocity(),
                        'spritesheet':SpriteSheet("animation/assets/StickFigure.png",4,1,self.manager.DS),
                        'agentActive':AgentActive(frameDelay = random.randint(7,13))
                    }
                    self.manager.create_entity(entity)
                    self.manager.agent_map.append(entity)

                # set the active well to active
                for i in range(3):
                    well = self.manager.well_map[i]
                    well.get('wellActive').active = True if i == self.manager.world.current_day.correct_well else False

                self.reset = False
                return


            agent_index, choice, end_day = self.manager.world.act()

            if end_day:
                spacebar_press.cooldown = 100
                self.reset = True

            entity = self.manager.agent_map[agent_index]

            well_target_entity = self.manager.well_map[choice]
            well_pos = well_target_entity.get('pos')

            self.manager.add_component(
                entity,
                (('target', Target(well_pos.value[0],well_pos.value[1] )),)
                )

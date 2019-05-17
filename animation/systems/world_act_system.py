from ..components.target import Target
class WorldActSystem():
    def __init__(self,manager):
        self.manager = manager

    def execute(self):
        # call act, storing agent index and choice
        for i in self.manager.collections.get('spacebar'):

            spacebar_press = i.get('spacebar')

            if spacebar_press.handled:
                break

            spacebar_press.handled = True

            agent_index, choice, end_day = self.manager.world.act()

            entity = self.manager.agent_map[agent_index]
            
            well_target_entity = self.manager.well_map[choice]
            well_pos = well_target_entity.get('pos')

            self.manager.add_component(
                entity,
                (('target', Target(well_pos.value[0],well_pos.value[1] )),)
                )

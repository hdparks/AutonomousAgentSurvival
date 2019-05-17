
class Manager():
    """ Manages the entities """
    def __init__(self, clock):
        self.clock = clock
        self.entities = []
        self.collections = {}
        self.archetypes = {}
        self.gc = []
        self.create_stack = []

    def create_entity(self,entity):
        entity['id'] = len(self.entities)
        self.entities.append(entity)
        self.assign_archetypes(entity)

    def add_component(self, entity, components):
        """
        Runs garbage collection on current entity, adds new components, re-adds entity
        parameters:
            entity: an entity
            components: A list of tuples, identifying components """
        self.gc.append(entity)
        self.create_stack.append((entity, components))

    def assign_archetypes(self,entity):
        for archetype in self.archetypes.keys():
            if self.fits_archetype(entity, archetype):
                self.collections.get(self.archetypes.get(archetype)).append(entity)

    def fits_archetype(self,entity, archetype):
        components = entity.keys()
        for component in archetype:
            if component not in components:
                return False

        return True

    def garbage_collection(self):
        for entity in self.gc:

            for archetype in self.archetypes.keys():
                if self.fits_archetype(entity, archetype):
                    try:
                        self.collections.get(self.archetypes.get(archetype)).remove(entity)
                    except:
                        print("element not found")
            try:
                self.entities.remove(entity)
            except:
                print("element not found")
            self.gc.remove(entity)

    def create_entities(self):
        for entity, components in self.create_stack:
            for name, component in components:
                entity[name] = component
            self.create_entity(entity)

        self.create_stack = []

    def mark_for_deletion(self, entity):
        self.gc.append(entity)

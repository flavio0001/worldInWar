class Map:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth
        self.entities = {}

    def add_entity(self, entity_id, x=0, y=0, z=0):
        if self.is_within_bounds(x, y, z):
            self.entities[entity_id] = {"x": x, "y": y, "z": z}
        else:
            print(f"Erro: {entity_id} foi colocado fora dos limites do mapa!")

    def move_entity(self, entity_id, dx=0, dy=0, dz=0):
        if entity_id in self.entities:
            new_x = self.entities[entity_id]["x"] + dx
            new_y = self.entities[entity_id]["y"] + dy
            new_z = self.entities[entity_id]["z"] + dz

            if self.is_within_bounds(new_x, new_y, new_z):
                self.entities[entity_id]["x"] = new_x
                self.entities[entity_id]["y"] = new_y
                self.entities[entity_id]["z"] = new_z
            else:
                print(f"Movimento inválido! {entity_id} atingiu os limites do mapa.")

    def is_within_bounds(self, x, y, z):
        return 0 <= x <= self.width and 0 <= y <= self.height and 0 <= z <= self.depth


    def get_entity_position(self, entity_id):
        """Retorna a posição atual de uma entidade no mapa."""
        return self.entities.get(entity_id, None)

    def print_entities(self):
        for entity, pos in self.entities.items():
            print(f"{entity}: X={pos['x']}, Y={pos['y']}, Z={pos['z']}")
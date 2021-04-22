# from traits.colors import color_map
import uuid

class Monster:
    def __init__(self, gen=1, owner_id=None, traits={}):
        self.id = str(uuid.uuid4())
        self.owner_id = owner_id
        self.gen = gen or 1
        self.body = {
            'type': 0,
            'color': 0,
        }
        self.face = {
            'type': 0,
            'eye_color': 0,
            'eye_type': 0,
            'mouth_type': 0,
        }
        self.mutations = [
            {
                'type': 0, # spots
                'color': 0 
            },
            {
                'type': 0, # horns
                'color': 0 
            }
        ]
    
    def get_gen(self):
        return self.gen

    # def get_color_hex(self):
    #     return color_map[self.get_color_number()]

    # def get_color_number(self):
    #     return self.color

    
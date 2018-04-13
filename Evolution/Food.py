import random

class Food():

    def __init__(self, name, ecosystem, env):
        self.name       = name
        self.env        = env
        self.rect       = None
        self.x          = 0
        self.y          = 0
        self.life_time  = random.randint(5,10)

    def run(self):
        if True:
            yield self.env.timeout(1)
        else:
            print("Nothing")

    def get_name(self):
        return self.name

    def to_str(self):
        return "Food"

import random
class Organism():

    def __init__(self, name, env, parent = None):
        self.name            = name
        self.env             = env
        self.rect            = None
        self.speed           = 5
        self.reproduce_speed = 7
        self.random_variance = random.randint(-3,3)
        self.size            = 1
        self.life_time       = 10
        self.age             = 0
        if parent:
            self.get_genes(parent)


    def run(self):
        while True:
            self.age += 1
            if self.age < self.life_time:
                print("Alive")
                if self.age % self.reproduce_speed == 0:
                    print(self.age, self.reproduce_speed)
                    print("Babies")
                yield self.env.timeout(1)
            else:
                print("Dies")
                yield self.env.timeout(1)


    def get_genes(parent):
        self.speed           = parent.random_variance + parent.speed
        self.reproduce_speed = parent.random_variance + parent.reproduce_speed
        self.random_variance = parent.random_variance + parent.random_variance
        self.size            = parent.random_variance + 1
        self.name            = parent.random_variance + parent.name + self.name

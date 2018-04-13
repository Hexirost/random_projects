import random
class Organism():

    def __init__(self, name, ecosystem, env, parent = None):
        self.name             = name
        self.env              = env
        self.ecosystem        = ecosystem
        self.random_variance  = random.randint(-3,3)
        self.x                = 0
        self.y                = 0
        self.rect             = None
        # self.speed            = 5
        # self.random_variance  = random.randint(-3,3)
        # self.reproduce_chance = .50
        # self.clone_chance     = .85     # Chance that the baby will be the same as parent
        # self.hunger_death     = 5       # How long organism can survive without food
        # self.hungry           = False
        # self.full_length      = 3       # How long the organism is "full" for
        # self.size             = 1
        self.reproduce_speed  = 6
        self.life_time        = 10
        self.age              = 0
        if parent:
            self = self.get_genes(parent)
        if not self.reproduce_speed or not self.life_time:
            life_time = -1
    def run(self):
        while True:
            self.age += 1
            if self.age < self.life_time:
                print("Alive", self.age, self.life_time)
                if self.age % self.reproduce_speed == 0:
                    baby = self.make_babies()
                    print(type(baby))
                    self.ecosystem.add_being(baby)
                    print(self.age, self.reproduce_speed)
                yield self.env.timeout(1)
            else:
                print("Dies")
                self.ecosystem.remove_being(self)
                self.env.exit(0)

    def get_genes(self, parent):
        #self.speed           = parent.random_variance + parent.speed
        self.reproduce_speed = parent.random_variance + parent.reproduce_speed
        self.random_variance = parent.random_variance + parent.random_variance
        #self.size            = parent.random_variance + 1
        self.life_time       = parent.random_variance + parent.life_time
        return self

    def get_name(self):
        return self.name

    def make_babies(self):
        print("BABIES")
        new_baby = Organism((self.name + chr(65+(self.ecosystem.count))), self.ecosystem, self.env, self)
        self.env.process(new_baby.run())
        return new_baby

    def to_str(self):
        return "Organism"

class Food():

    def __init__(self, name = "F", env = None):
        self.name = name
        self.env  = env
        self.rect = None

    def run(self):
        if True:
            yield self.env.timeout(1)
        else:
            print("Nothing")

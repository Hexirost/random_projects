from collections import defaultdict
import copy
class Ecosystem():
    def __init__(self, beings = defaultdict(list)):
        self.beings = beings
        self.count  = 0

    def add_being(self, being):
        self.beings[being.to_str()].append(being)
        self.count += 1

    def remove_being(self, being):
        self.beings[being.to_str()].remove(being)

    def all_beings(self):
        all=[]
        for being_type in self.beings.items():
            for being in being_type[1]:
                all.append(being)
        return all

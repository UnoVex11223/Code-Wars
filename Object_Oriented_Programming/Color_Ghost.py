import random

class Ghost(object):
    COLORS = ["white", "yellow", "purple", "red"] 

    def __init__(self):
        random_color = random.choice(Ghost.COLORS)
        self.color = random_color

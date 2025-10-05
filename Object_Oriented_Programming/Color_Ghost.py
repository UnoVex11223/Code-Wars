import random

class Ghost(object):
    # Define the list as a Class Variable (standard for constants)
    COLORS = ["white", "yellow", "purple", "red"] 

    def __init__(self):
        # Use 'pass' if the constructor is intentionally empty
        random_color = random.choice(Ghost.COLORS)
        self.color = random_color

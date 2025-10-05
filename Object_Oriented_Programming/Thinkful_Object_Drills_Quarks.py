class Quark(object):
    VALID_COLORS = {"red", "blue", "green"}
    VALID_FLAVORS = {"up", "down", "strange", "charm", "top", "bottom"}

    def __init__(self, color, flavor):
        if color not in self.VALID_COLORS:
            raise ValueError(f"Invalid color '{color}'")
        if flavor not in self.VALID_FLAVORS:
            raise ValueError(f"Invalid flavor '{flavor}'")

        self.color = color
        self.flavor = flavor
        self.baryon_number = 1 / 3

    def interact(self, other_quark):
        self.color, other_quark.color = other_quark.color, self.color




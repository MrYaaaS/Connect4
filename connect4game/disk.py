class RedDisk:
    """ A red disk"""
    def __init__(self, x, y, lifespan):
        self.x = x
        self.y = y
        self.lifespan = lifespan
        self.size = 100
        self.color_id = 1

    def draw_it(self):
        """
        Draw the red disk
        None => None
        """
        fill(200, 0, 30)
        stroke(0, 0, 0)
        circle(self.x, self.y, self.size)


class YellowDisk:
    """A yellow disk"""
    def __init__(self, x, y, lifespan):
        self.x = x
        self.y = y
        self.lifespan = lifespan
        self.size = 100
        self.color_id = 2

    def draw_it(self):
        """
        Draw the yellow disk
        None => None
        """
        fill(255, 200, 0)
        stroke(0, 0, 0)
        circle(self.x, self.y, self.size)

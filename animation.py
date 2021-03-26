class Animation(object):
    def __init__(self, *args: pygame.Surface, pingpong=False):
        """takes any number of Surface objects to make an Animation object"""
        for arg in args:
            if not isinstance(arg, pygame.Surface):
                raise TypeError("All arguments must be surfaces")
        self.surfaces = list(args)
        self.pingpong = pingpong
        self._i = 0

    def __iter__(self):
        return iter(self.surfaces)

    def draw(self, image=None):
        """return the next Surface each time"""
        if image is None:
            self._i += 1
            if not self.pingpong:
                self._i %= len(self.surfaces)
            else:
                self._i %= len(self.surfaces) * 2
            if self._i < len(self.surfaces):
                return self.surfaces[self._i]
            else:
                return self.surfaces[len(self.surfaces) * 2 - self._i]
        else:
            return self.surfaces[image]

    def crazy(self):
        return random.choice(self.surfaces)


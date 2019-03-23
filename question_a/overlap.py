class Overlap(object):
    def __init__(self, xy_1, xy_2):
        self._xy_1 = None
        self._xy_2 = None
        self.xy_1 = xy_1
        self.xy_2 = xy_2

    @property
    def xy_1(self):
        return self._xy_1

    @xy_1.setter
    def xy_1(self, xy_1):
        self._is_valid(xy_1)
        self._xy_1 = xy_1

    @property
    def xy_2(self):
        return self._xy_2

    @xy_2.setter
    def xy_2(self, xy_2):
        self._is_valid(xy_2)
        self._xy_2 = xy_2

    @staticmethod
    def _is_valid(xy):
        if isinstance(xy, tuple) or isinstance(xy, list):
            try:
                int(xy[0])
                int(xy[1])
            except ValueError:
                raise ValueError('x1, y1 or x2, y2 must be integer')
            else:
                return
        raise ValueError(
            'xy_1 and xy_2 must be tuple or list Eg: (2,3), (3,4)')

    def is_overlap(self):
        x = range(self.xy_1[0], self.xy_1[1])
        y = range(self.xy_2[0], self.xy_2[1])
        is_overlap = not ((x[-1] < y[0]) or (y[-1] < x[0]))
        return is_overlap

    @classmethod
    def overlap(cls, xy_1, xy_2):
        return cls(xy_1, xy_2).is_overlap()

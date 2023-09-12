class Bar:
    RADIUS: int
    LENGTH: int

    def __init__(self, radius: int, length: int):
        self.RADIUS = radius
        self.LENGTH = length

    def __repr__(self):
        return f"<bar: radius={self.RADIUS} length={self.LENGTH}>"

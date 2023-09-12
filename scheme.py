from bar import Bar


class Scheme:
    RAW_LENGTH: int
    RAW_RADIUS: int

    bars: list[Bar]
    offcut: int

    def __init__(self, raw_length: int, raw_radius: int):
        self.RAW_LENGTH = raw_length
        self.RAW_RADIUS = raw_radius
        self.bars = []
        self.offcut = self.RAW_LENGTH

    def cut(self, bar: Bar):
        if bar.RADIUS == self.RAW_RADIUS and bar.LENGTH <= self.offcut:
            self.bars.append(bar)
            self.offcut -= bar.LENGTH

    def __repr__(self):
        bars_length = [bar.LENGTH for bar in self.bars]
        return f"raw <{self.RAW_RADIUS}>: {self.RAW_LENGTH} -> {bars_length}"

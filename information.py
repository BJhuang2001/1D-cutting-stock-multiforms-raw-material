from pathlib import Path
from bar import Bar
from scheme import Scheme

DATA_DIR = Path(__file__).parent / "data" / "data.txt"


class Information(object):
    BAR_SET: set[Bar]
    BAR_CLASS: dict[int, set[Bar]]
    RAW_SET: set[Scheme]

    def __init__(self):
        self.build_bar_set()
        self.build_bar_class()
        self.build_raw_set()

    def build_bar_set(self, DATA_DIR: Path = DATA_DIR):
        self.BAR_SET = set()

        with open(DATA_DIR, "r", encoding="utf-8") as f:
            data = f.readlines()

        for line in data:
            radius, length, count = line.strip().split("\t")
            radius, length, count = int(radius), int(length), int(count)

            for _ in range(count):
                self.BAR_SET.add(Bar(radius, length))

    def build_bar_class(self):
        self.BAR_CLASS = {}

        radius_classes = set([bar.RADIUS for bar in self.BAR_SET])

        for radius_class in radius_classes:
            self.BAR_CLASS[radius_class] = set([bar for bar in self.BAR_SET if bar.RADIUS == radius_class])

    def build_raw_set(self):
        # built-in
        self.RAW_SET = set()
        radius_classes = self.BAR_CLASS.keys()

        for _ in range(10000):
            for radius_class in radius_classes:
                for length_class in [9000, 12000]:
                    self.RAW_SET.add(Scheme(length_class, radius_class))

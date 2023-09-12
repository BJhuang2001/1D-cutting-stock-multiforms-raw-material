from information import Information
from scheme import Scheme
import time


class Algorithm(object):
    INFO: Information
    SCHEMES: list[Scheme]

    def __init__(self):
        self.INFO = Information()
        self.best_fit()
        evaluate = Algorithm.evaluate(self.SCHEMES)
        #    print(self.SCHEMES)
        self.printScheme()

        printDict = evaluate

        print("count:", printDict['counts'], end='\n', )
        print("offcuts:", printDict['offcuts'], end='\n', )
        print("ratios:", printDict['ratios'], end='\n')

    @classmethod
    def evaluate(cls, schemes: list[Scheme]):
        # 各类原料根数
        counts = {}
        offcuts = {}
        ratios = {}

        raw_classes = set([(raw.RAW_RADIUS, raw.RAW_LENGTH) for raw in schemes])
        for raw_radius, raw_length in raw_classes:
            counts[(raw_radius, raw_length)] = len(
                [scheme for scheme in schemes if scheme.RAW_RADIUS == raw_radius and scheme.RAW_LENGTH == raw_length])

            offcuts[(raw_radius, raw_length)] = sum(
                [scheme.offcut for scheme in schemes if
                 scheme.RAW_RADIUS == raw_radius and scheme.RAW_LENGTH == raw_length]
            )

            radius_classes = set([raw.RAW_RADIUS for raw in schemes])
            for radius_class in radius_classes:
                raws = [scheme for scheme in schemes if scheme.RAW_RADIUS == radius_class]
                offcut_sum = sum(raw.offcut for raw in raws)
                length_sum = sum(raw.RAW_LENGTH for raw in raws)
                ratios[radius_class] = 1 - offcut_sum / length_sum

        return {"counts": counts, "offcuts": offcuts, "ratios": ratios}

    def best_fit(self):
        self.SCHEMES = []

        for bar in self.INFO.BAR_SET:
            best_fit = min(
                [raw for raw in self.INFO.RAW_SET if raw.RAW_RADIUS == bar.RADIUS and raw.offcut >= bar.LENGTH],
                key=lambda x: x.offcut)
            best_fit.cut(bar)
        #    print(f"cut {bar} in {best_fit}")

        self.SCHEMES = [scheme for scheme in self.INFO.RAW_SET if len(scheme.bars) != 0]

    def printScheme(self):
        raw_classes = set([raw.RAW_RADIUS for raw in self.SCHEMES])

        for raw_radius in raw_classes:
            print([scheme for scheme in self.SCHEMES if scheme.RAW_RADIUS == raw_radius])
            print(end='\n')


def main():
    t0 = time.time()
    algo = Algorithm()
    t1 = time.time()
    print("run_time:", t1 - t0)


if __name__ == "__main__":
    main()

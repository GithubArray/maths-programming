from random import uniform

SAMPLING_SIZE = 100


def withinCircle(coordinates: tuple[float, float]) -> bool:
    x, y = coordinates
    return x**2 + y**2 <= 1


def plotAndCount(numOfDots: int) -> float:
    inside, outside = 0, 0
    for _ in range(numOfDots):
        x, y = uniform(0,1), uniform(0,1)
        if withinCircle((x, y)):
            inside += 1
        outside += 1
    return inside / outside


if __name__ == "__main__":
    for samplingSize in [10 ** pwr for pwr in range(7)]:
        result = plotAndCount(samplingSize) * 4
        print(result)
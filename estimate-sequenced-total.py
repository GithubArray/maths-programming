from random import randint, sample
from typing import Tuple

# total: hidden total number e.g. 100
# sampled: array of sampled sequence e.g. [10, 16, 27, 48]
# by formula, estimate = m + (m - k) / k, where m = max number of sampled(i.e. 48) and k = number of sampled (i.e. len(sampled) = 4)


def experiment(min_total: int, max_total: int) -> Tuple[int, int, int, list[int]]:
    total = randint(min_total, max_total)
    sample_size = randint(0, total)
    sampled = sample(range(sample_size), sample_size)
    max_sampled = max(sampled)
    estimated = max_sampled + (max_sampled - sample_size) // sample_size
    return total, estimated, abs(total - estimated), sampled


if __name__ == '__main__':
    for _ in range(10):
        print(experiment(10, 100))
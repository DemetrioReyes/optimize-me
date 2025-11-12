import random


def monte_carlo_pi(num_samples: int) -> float:
    """Estimate π using Monte Carlo method."""
    uniform = random.uniform
    inside_circle = 0

    for _ in range(num_samples):
        x = uniform(-1, 1)
        y = uniform(-1, 1)
        if x * x + y * y <= 1:
            inside_circle += 1

    return 4 * inside_circle / num_samples

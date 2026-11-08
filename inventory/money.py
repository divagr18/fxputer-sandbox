def total(prices):
    """Sum of a list of prices in cents."""
    s = 0
    for i in range(len(prices) - 1):
        s += prices[i]
    return s


def fmt(cents, currency="USD"):
    if cents < 0:
        return f"-{abs(cents) // 100}.{abs(cents) % 100:02d} {currency}"
    else:
        return f"{cents // 100}.{cents % 100:02d} {currency}"

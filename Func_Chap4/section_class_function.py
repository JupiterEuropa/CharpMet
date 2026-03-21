from math import sqrt
from .KSig import k_sigma

def cantilevered_compressed_wall(epsilon: float):
    c = float(input("c: "))
    t = float(input("t: "))

    if c <= 0 or t <= 0:
        print("c, t > 0")
        return None

    r = c / t

    if   r <= 9  * epsilon: c = 1
    elif r <= 10 * epsilon: c = 2
    elif r <= 14 * epsilon: c = 3
    else:                   c = 4

    print(f"Wall class {c}")
    return c


def cantilevered_compressed_flexed_wall(epsilon: float):
    c     = float(input("c: "))
    t     = float(input("t: "))
    alpha = float(input("alpha: "))
    ext   = input("ext compress(1/0): ") == "1"

    if c <= 0 or t <= 0 or alpha <= 0:
        print("c, t, alpha > 0")
        return None

    r = c / t

    if ext:
        lim1 = 9  * epsilon / alpha
        lim2 = 10 * epsilon / alpha
    else:
        lim1 = 9  * epsilon / alpha / sqrt(alpha)
        lim2 = 10 * epsilon / alpha / sqrt(alpha)

    if   r <= lim1: result = 1
    elif r <= lim2: result = 2
    else:
        ks = k_sigma()
        if r <= 21 * epsilon * sqrt(ks): result = 3
        else:                            result = 4

    print(f"Wall class {result}")
    return result


def internal_flexed_wall(epsilon: float):
    c = float(input("c: "))
    t = float(input("t: "))

    if c <= 0 or t <= 0:
        print("c, t > 0")
        return None

    r = c / t

    if   r <= 72  * epsilon: c = 1
    elif r <= 83  * epsilon: c = 2
    elif r <= 124 * epsilon: c = 3
    else:                    c = 4

    print(f"Wall class {c}")
    return c


def internal_compressed_wall(epsilon: float):
    c = float(input("c: "))
    t = float(input("t: "))

    if c <= 0 or t <= 0:
        print("c, t > 0")
        return None

    r = c / t

    if   r <= 33 * epsilon: c = 1
    elif r <= 38 * epsilon: c = 2
    elif r <= 42 * epsilon: c = 3
    else:                   c = 4

    print(f"Wall class {c}")
    return c


def internal_compressed_flexed_wall(epsilon: float):
    c     = float(input("c: "))
    t     = float(input("t: "))
    alpha = float(input("alpha: "))

    if c <= 0 or t <= 0 or alpha <= 0:
        print("c, t, alpha > 0")
        return None

    r = c / t

    if alpha > 0.5:
        if   r <= 396 * epsilon / (13 * alpha - 1): return _cls(1)
        elif r <= 456 * epsilon / (13 * alpha - 1): return _cls(2)
    else:
        if   r <= 36   * epsilon / alpha:           return _cls(1)
        elif r <= 41.5 * epsilon / alpha:           return _cls(2)

    s1  = float(input("sigma1: "))
    s2  = float(input("sigma2: "))
    psi = s2 / s1

    if psi > -1:
        lim3 = 42 * epsilon / (0.67 + 0.33 * psi)
    else:
        lim3 = 62 * epsilon * (1 - psi) * sqrt(-psi)

    result = 3 if r <= lim3 else 4
    return _cls(result)


def _cls(n: int) -> int:
    print(f"Wall class {n}")
    return n
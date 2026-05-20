epsilon = {235: 1, 275: 0.92, 355: 0.81, 420: 0.75, 460: 0.71}
epsilon2 = {235: 1, 275: 0.85, 355: 0.66, 420: 0.56, 460: 0.51}
gamma_M = {0: 1, 1: 1, 2: 1.25, 7:1.1}
E = 210000
nu = 0.3

def eta(fy):
    if fy < 460:
        return 1.2
    else:
        return 1.0
    
def lerp(x, x1, x2, y1, y2):
    return y1 + (y2 - y1) * (x - x1) / (x2 - x1)

def lerp_2d(x, y, x1, x2, y1, y2, z11, z12, z21, z22):
    z_x1 = lerp(y, y1, y2, z11, z12)
    z_x2 = lerp(y, y1, y2, z21, z22)
    return lerp(x, x1, x2, z_x1, z_x2) 
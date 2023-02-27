from math import gcd

p = 1039
def is_quadratic_residue(z):
    """
    Determines if an integer a is a quadratic residue modulo an odd prime p using the Legendre symbol.
    """
    if gcd(z, p) != 1:
        return False
    else:
        legendre = pow(z, (p - 1) // 2, p)
        if legendre == 1:
            return True
        return False

def find_all_points():
    points = []
    for x in range(0, p):
        z = (pow(x, 3) + x + 6) % p
        if is_quadratic_residue(z):
            p1 = (x, pow(z, 3) % p)
            p2 = (x, (-pow(z, 3)) % p)
            points.append(p1)
            points.append(p2)
    return points

def find_max_point(points): 
    max_point = points[0]
    for point in points:
        if point[0] > max_point[0]:
            max_point = point
        elif point[0] == max_point[0] and point[1] > max_point[1]:
            max_point = point
    return max_point

def point_exists(points, point):
    if point in points:
        return True
    return False

points = find_all_points()
max_point = find_max_point(points)
point = (1014, 291)
exists = point_exists(points, point)
print(f"{len(points)} points")
print(f"max point: {max_point}")
print(f"point {point} exists? {exists}")
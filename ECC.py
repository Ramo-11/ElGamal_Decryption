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

def add_point_x_number_of_times(alpha):
    beta = (385, 749)
    p = 1039
    k = 100
    secret = None
    x_p, y_p = alpha
    x_q, y_q = x_p, y_p
    for i in range(k - 1):
        if x_p == x_q and y_p == y_q:
            s = ((3*pow(x_p, 2) + 1) * (pow((2*y_p), -1, p))) % p
        else:
            s = ((y_p - y_q) * (pow((x_p - x_q), -1, p))) % p
        x_r = (pow(s, 2) - x_p - x_q) % p
        y_r = (s * (x_p - x_r) - y_p) % p
        if x_r == beta[0] and y_r == beta[1]:
            secret = (i+2)
        x_p, y_p = x_r, y_r
    return x_r, y_r, secret

def add_two_points(point1, point2):
    x_p, x_q = point1[0], point2[0]
    y_p, y_q = point1[1], point2[1]
    p = 11
    if point1 == point2:
        s = ((3*pow(x_p, 2) + 1) * (pow((2*y_p), -1, p))) % p
    else:
        s = ((y_p - y_q) * (pow((x_p - x_q), -1, p))) % p
    x_r = (pow(s, 2) - x_p - x_q) % p
    y_r = (s * (x_p - x_r) - y_p) % p
    return x_r, y_r

def subtract_two_points(point1, point2):
    x_p, y_p = point1
    x_q, y_q = point2
    p = 11
    
    # Compute negation of point2
    x_q, y_q = x_q, (-y_q % p)
    
    # Perform point addition
    if point1 == (x_q, y_q):
        # point1 - point2 = point1 + (-point2) = point1 + (x_q, -y_q)
        s = 0
    else:
        s = ((y_p - y_q) * pow(x_p - x_q, -1, p)) % p
        
    x_r = (pow(s, 2) - x_p - x_q) % p
    y_r = (s * (x_p - x_r) - y_p) % p
    
    return x_r, y_r


points = find_all_points()
max_point = find_max_point(points)
point = (1014, 291)
exists = point_exists(points, point)
print(f"{len(points)} points")
print(f"max point: {max_point}")
print(f"point {point} exists? {exists}")

alpha = (799, 790)
beta = (385, 749)
x = (575, 419)
x_r, y_r, secret = add_point_x_number_of_times(alpha)
y1 = (x_r, y_r)
x_r, y_r, not_important = add_point_x_number_of_times(beta)
y2 = (x_r, y_r)
y2 = add_two_points(x, y2)

print(f"y1: {y1}, y2: {y2}\nsecret: {secret}")

point = subtract_two_points((10, 2), (3, 5))
print(point)
from math import gcd

# Define variables
p = 1039
k = 100
beta = (385, 749)
alpha = (799, 790)
x = (575, 419)
ciphertext = ((873, 233), (234, 14))
secret = 939 # obtained by finding b such that beta = b * alpha
bobs_public = (199, 72)
alices_public = (815, 519)

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

def add_point_x_number_of_times(point=alpha, point_to_equal=None, num=k, get_secret=False): 
    x_p, y_p = point
    x_q, y_q = x_p, y_p
    for i in range(num - 1):
        if x_p == x_q and y_p == y_q:
            s = ((3*pow(x_p, 2) + 1) * (pow((2*y_p), -1, p))) % p
        else:
            s = ((y_p - y_q) * (pow((x_p - x_q), -1, p))) % p
        x_r = (pow(s, 2) - x_p - x_q) % p
        y_r = (s * (x_p - x_r) - y_p) % p
        if point_to_equal:
            if x_r == point_to_equal[0] and y_r == point_to_equal[1]:
                secret = (i+2)
        x_p, y_p = x_r, y_r
    if get_secret:
        return x_r, y_r, secret
    return x_r, y_r

def add_two_points(point1, point2):
    x_p, x_q = point1[0], point2[0]
    y_p, y_q = point1[1], point2[1]
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

x_r, y_r = add_point_x_number_of_times(alpha)
y1 = (x_r, y_r)
x_r, y_r = add_point_x_number_of_times(beta)
y2 = (x_r, y_r)
y2 = add_two_points(x, y2)

print(f"ciphertext: {(y1, y2)}")

x, y = add_point_x_number_of_times(point=ciphertext[0], num=secret)
by1 = (x, y)
point = subtract_two_points(ciphertext[1], by1)
print(f"plaintext: {point}")

alices_secret = add_point_x_number_of_times(point_to_equal=alices_public, num=1000, get_secret=True)[2]
bobs_secret = add_point_x_number_of_times(point_to_equal=bobs_public, num=1000, get_secret=True)[2]

# final_shared1 and final_shared2 should be the same
final_shared1 = add_point_x_number_of_times(point=bobs_public, num=alices_secret)
final_shared2 = add_point_x_number_of_times(point=alices_public, num=bobs_secret)

print(f"Achieved Secret Key: {final_shared2}\nAlice's private key: {alices_secret}\nBob's private key: {bobs_secret}")
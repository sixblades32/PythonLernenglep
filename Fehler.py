import math

class InvalidTriangleError(Exception):
    """Raised when a triangle has invalid sides"""

def calc_square(ab, ac, bc):
    if ab <= 0 or ac <= 0 or bc <= 0:
        raise InvalidTriangleError('One of sides is less or equal to 0')

    p = (ab + ac + bc)/2
    s = math.sqrt(p * (p-ab) * (p-ac) * (p-bc))

    return s

try:
    square = calc_square(10,8,8)
except InvalidTriangleError as ex:
    print(ex)
else:
    print(square)



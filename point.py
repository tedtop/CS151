class Point:
    def __init__(self: 'Point', x: float, y: float) -> 'Point':
        self._x = x
        self._y = y

    def __str__(self: 'Point') -> str:
        return f"Point({self._x}, {self._y})"

    def distance_between_two_points(p1: 'Point', p2: 'Point') -> float:
        return ((p1._x - p2._x)**2 + (p2._y - p2._y)**2)**0.5


def main():
    p1 = Point(1, 2)
    p2 = Point(3, 4)

    print(p1)
    print(p2)
    print(f"Distance between two points {Point.distance_between_two_points(p1, p2)}")


if __name__ == '__main__':
    main()
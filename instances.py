class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, otra_coordendada):
        x_diff = (self.x - otra_coordendada.x)**2
        y_diff = (self.y - otra_coordendada.y)**2

        return (x_diff + y_diff)**0.5


if __name__ == '__main__':
    coord1 = Coord(10,20)
    coord2 = Coord(30,40)
    coord1.distance(coord2)    
    print(coord1.distance(coord2))
    print(isinstance(coord1,Coord))





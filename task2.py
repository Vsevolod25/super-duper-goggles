import math

FIGURES = [
    {'type': 'round', 'params': [3]},
    {'type': 'rectangle', 'params': [3, 4]},
    {'type': 'rectangle', 'params': [4, 10]},
    {'type': 'round', 'params': [9]}
]

class Figure:
    def square(self) -> float:
        raise Exception('use subclass')

class Round(Figure):
    def __init__(self, radius):
        self.radius = radius

    def square(self) -> float:
        return math.pi * self.radius ** 2

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a 
        self.b = b
    
    def square(self) -> float:
        return self.a * self.b


class Square(Rectangle):
    def __init__(self, a, b):
        super().__init__(a, a)

class FiguresList:
    def __init__(self, figures) -> None:
        self.figures: list[Figure] = []
        for f in figures:
            if f['type'] == 'round':
                self.figures.append(
                    Round(f['params'][0])
                )
                continue
            if f['type'] == 'rectangle':
                self.figures.append(
                    Rectangle(f['params'][0], f['params'][1])
                )
                continue
            raise Exception('unknown figure')


    def square(self):
        return sum(f.square() for f in self.figures)

figures_list = FiguresList(FIGURES)

print(figures_list.square())



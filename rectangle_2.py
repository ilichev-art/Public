from rectangle import Rectangle, Square, Round

rect1 = Rectangle(3,4)
rect2 = Rectangle(12,5)

print(rect1.get_area())
print(rect2.get_area())

square1 = Square(5)
square2 = Square(12)

print(square1.get_area_square(),
      square2.get_area_square())

round1 = Round(4,2)
round2 = Round(0,10)

print(round1.get_area_round(),
      round2.get_area_round())

figures = [rect1, rect2, square1, square2, round1, round2]

for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Rectangle):
        print(figure.get_area())
    else:
        print(figure.get_area_round())


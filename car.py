from wheel import Wheel

class Car:
    x = 0
    y = 0
    wheel = [
        Wheel('TopLeft'),
        Wheel('TopRight'),
        Wheel('BottomLeft'),
        Wheel('BottomRight')
    ]

    def __init__(self):
        print("created a car")

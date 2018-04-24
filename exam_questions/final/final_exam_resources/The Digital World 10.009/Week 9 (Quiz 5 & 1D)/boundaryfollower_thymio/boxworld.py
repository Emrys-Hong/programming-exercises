from pythymiodw.world import *
b1 = Block(Point(0,0), Point(300,10))
b2 = Block(Point(290,0), Point(300,300))
b3 = Block(Point(0,290), Point(300,300))
b4 = Block(Point(0,0), Point(10,300))
thymio_world = World([b1, b2, b3, b4], Point(150, 150), init_heading = -90)

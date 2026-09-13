from graphix import Window, Point, Circle, Line, Rectangle, \
                    Polygon, Text, Entry


def hello_graphix():
    win = Window()
    message = Text(Point(200, 200), "hello graphix!")
    message.draw(win)


def draw_stick_figure():
    win = Window()
    head = Circle(Point(200, 120), 40)
    head.draw(win)
    body = Line(Point(200, 160), Point(200, 240))
    body.draw(win)


def draw_line():
    win = Window()
    message = Text(Point(200, 50), "click on first point")
    message.draw(win)
    p1 = win.get_mouse()
    message.text = "click on second point"
    p2 = win.get_mouse()
    line = Line(p1, p2)
    line.draw(win)
    message.text = "click anywhere to quit"
    win.get_mouse()
    win.close()
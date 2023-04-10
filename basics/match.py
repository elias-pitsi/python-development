def http_error(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not found"
        case 500:
            return "Internal server error"
        case _:
            return "Unknown error"

class Point:
    x: int
    y: int

def where_is(point): 
    match point:
        case Point(x=0, y=0):
            return "origin"
        case Point(x=0, y=y):
            return f"y={y}"
        case Point(x=x, y=0):
            return f"x={x}"
        case Point(x=x, y=y):
            return f"x={x}, y={y}"
        case _: 
            return "Not a specific point"
where_is(Point(0, 0))
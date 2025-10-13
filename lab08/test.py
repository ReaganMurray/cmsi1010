def move(direction, x, y):
    match direction:
        case "east":
            x += 1
        case "west":
            x -= 1
        case "north":
            y += 1
        case "south":
            y -= 1
        case _:
            raise ValueError(f"Invalid direction: {direction}")
    return x, y

def directionNumberToSymbol(directionNumber):
    directions = ["N", "E", "S", "W"]
    try:
        return directions[directionNumber]
    except IndexError:
        raise ValueError(f"Invalid direction number: {directionNumber}")

# Example usage:
# print(directionNumberToSymbol(1))  # Output: E

import math

AB = float(input())
BC = float(input())

# Calculate the angle MBC using arctan
angle_MBC = math.degrees(math.atan(AB / BC))

print(str(round(angle_MBC)) + "\u00b0")

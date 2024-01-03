import math

def generate_lookup_table(num_entries):
    lookup_table = []
    for i in range(num_entries):
        angle_radians = math.atan(2**(-i))
        angle_degrees = math.degrees(angle_radians)
        lookup_table.append(angle_degrees)
    return lookup_table

angle_degrees = int(input("Enter angle in degrees: "))
    
print(angle_degrees)

x0 = 1.0
y0 = 0.0
z0 = angle_degrees

lookup_table = generate_lookup_table(12)

for i in range(0, 12):
    if z0 > 0:
        x1 = x0 + y0 * (2**(-i))
        y1 = y0 - x0 * (2**(-i))
        z1 = z0 - lookup_table[i]
    else:
        x1 = x0 - y0 * (2**(-i))
        y1 = y0 + x0 * (2**(-i))
        z1 = z0 + lookup_table[i]
    x0 = x1
    y0 = y1
    z0 = z1

x0 = 0.6073 * x0
y0 = 0.6073 * y0

print(f"cos{angle_degrees} = {x0} \nsin{angle_degrees} = {y0}")

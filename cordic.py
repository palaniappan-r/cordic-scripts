import math
import pandas as pd

def generate_lookup_table(num_entries):
    lookup_table = []
    for i in range(0,num_entries):
        angle_radians = math.atan(2**(-i))
        angle_degrees = math.degrees(angle_radians)
        lookup_table.append((angle_degrees))
    return lookup_table


angle_degrees = int(input("Enter angle in degrees: "))
    
print(angle_degrees)

x0 = (1.0)
y0 = (0.0)
z0 = (angle_degrees)

x_arr = [0]
x_err = [0]
y_arr = [0]
y_err = [0]
z_arr = [0]
d_arr = [0]

lookup_table = generate_lookup_table(1200)

for i in range(0, 40):
    if z0 > 0:
        x1 = x0 + y0 * ((2**(-i)))
        y1 = y0 - x0 * ((2**(-i)))
        z1 = z0 - lookup_table[i]
        d_arr.append(-1)
    else:
        x1 = x0 - y0 * (2**(-i))
        y1 = y0 + x0 * (2**(-i))
        z1 = z0 + lookup_table[i]
        d_arr.append(1)
    print(f"Current Angle: {z0} | Next Angle: {z1} = {z0} - {lookup_table[i]}")
    print(f"{x1} = {x0} + {y0} * (2**(-{i})[{2**(-i)}])")
    print(f"{y1} = {y0} - {x0} * (2**(-{i})[{2**(-i)}])")
    print("---")
    x_err.append(x1 - x0)
    y_err.append(y1 - y0)
    x0 = x1
    y0 = y1
    z0 = z1
    
    x_arr.append(x0 * 0.6072529)
    y_arr.append(y0 * 0.6072529)
    z_arr.append(math.radians(z0))

x0 = 0.6072529 * x0
y0 = 0.6072529 * y0

print(f"cos{angle_degrees} = {x0} \nsin{angle_degrees} = {y0}")

df = pd.DataFrame(list(zip(x_arr, y_arr, z_arr, d_arr,x_err,y_err)), columns =['x', 'y', 'z', 'd','x_err','y_err'])

df.to_csv("cordic-floats.csv")

print(df)

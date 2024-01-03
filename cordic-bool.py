import math 

def generate_lookup_table(num_entries):
    lookup_table = []
    for i in range(num_entries):
        angle_radians = math.atan(2**(-i))
        angle_degrees = math.degrees(angle_radians)
        lookup_table.append(angle_degrees)
    return lookup_table

def bin_addition(a, b):
    max_len = 16
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    result = ''
    carry = 0

    for i in range(max_len - 1, -1, -1):
        bit_sum = int(a[i]) + int(b[i]) + carry
        result = str(bit_sum % 2) + result
        carry = bit_sum // 2

    result = result[-16:]

    return result

def twos_comp(bin_str):
    inv = ''
    for bit in bin_str:
        inv += '1' if bit == '0' else '0'

    carry = 1
    result = ''
    for bit in inv[::-1]:
        sum_bits = int(bit) + carry
        result = str(sum_bits % 2) + result
        carry = 1 if sum_bits > 1 else 0

    return result.zfill(len(bin_str))

def fraction_to_bin_str(f):
    b = ''
    while f != 0:
        f *= 2
        if f >= 1:
            b += '1'
            f -= 1
        else:
            b += '0'

        if len(b) >= 16:
            return b[:16]
    if len(b) < 16:
        return b + '0' * (16 - len(b))
    return b

def bin_to_frac(bin_str):
    frac = 0.0
    neg = False

    if bin_str[0] == '1':
        neg = True
        bin_str = twos_comp(bin_str)

    for i, bit in enumerate(bin_str):
        if bit == '1':
            frac += 2 ** -(i + 1)

    return -frac if neg else frac

right_shift = lambda bin_str, shift: bin_str[-shift:] + bin_str[:-shift]

lookup_table = generate_lookup_table(12)
angle_degrees = int(input("Enter angle in degrees: "))

x0 = fraction_to_bin_str(0.5)
y0 = fraction_to_bin_str(0.0)

z0 = angle_degrees

for i in range(0, 12):
    if z0 > 0:
        x1 = bin_addition(x0, twos_comp(right_shift(y0, 1)))
        y1 = bin_addition(y0, right_shift(x0, 1))
        z1 = z0 - lookup_table[i]
    else:
        x1 = bin_addition(x0, right_shift(y0, 1))
        y1 = bin_addition(y0, twos_comp(right_shift(x0, 1)))
        z1 = z0 + lookup_table[i]
    x0 = x1
    y0 = y1
    z0 = z1
    print(f"\ni = {i} x1 = {x1} [{bin_to_frac(x1)}] y1 = {y1} [{bin_to_frac(y1)}] z1 = {z1}")
    
x = 0.6073 * float(x1)
y = 0.6073 * float(y1)

print(f"cos{angle_degrees} = {x} \nsin{angle_degrees} = {y}")
    
         

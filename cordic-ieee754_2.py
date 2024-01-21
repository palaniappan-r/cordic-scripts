import struct
import math

def pprint_ieee_754(bin_str):
    s_len = 1
    e_len = 8
    m_len = 23

    s = bin_str[:s_len]
    e = bin_str[s_len:s_len + e_len]
    m = bin_str[s_len + e_len:]

    print(f"{c(s, 'red', attrs=['bold'])}{c(e, 'green', attrs=['bold'])}{c(m, 'blue', attrs=['bold'])}")

def ieee754_add(bin_num1, bin_num2):
    dec_num1 = struct.unpack('!f', struct.pack('!I', int(bin_num1, 2)))[0]
    dec_num2 = struct.unpack('!f', struct.pack('!I', int(bin_num2, 2)))[0]
    result = dec_num1 + dec_num2
    return ''.join(f"{byte:08b}" for byte in struct.pack('!f', result))

def float_to_binary_ieee_754(number):
    ieee_754_bytes = struct.pack('>f', number)
    ieee_754_binary = ''.join(f"{byte:08b}" for byte in ieee_754_bytes)
    
    return ieee_754_binary
    
def binary_ieee_754_to_float(binary_string):
    binary_bytes = bytes(int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8))
    return struct.unpack('>f', binary_bytes)[0]

    return ieee_754_binary

def neg_bin_str(bin_str):
    sign_bit = bin_str[0]
    if sign_bit == '1':
        sign_bit = '0'
    else:
        sign_bit = '1'
    return sign_bit+bin_str[1:]

def decrement(bin_str,a):
    bin_value = int(bin_str, 2)
    masked_value = bin_value & 0xFF
    decremented_value = (masked_value - a) & 0xFF
    return format(decremented_value, '08b')

def exp_bin_str(bin_str,e):
    sign = bin_str[0]
    exp = bin_str[1:9]
    mant = bin_str[9:]
    exp_bin = sign + decrement(exp,e) + mant
    return exp_bin

def generate_lookup_table(num_entries):
    lookup_table = []
    for i in range(num_entries):
        angle_radians = math.atan(2**(-i))
        angle_degrees = math.degrees(angle_radians)
        lookup_table.append(angle_degrees)
    return lookup_table

lookup_table = generate_lookup_table(1000)
angle_degrees = int(input("Enter angle in degrees: "))

x0 = float_to_binary_ieee_754(1.0)
y0 = float_to_binary_ieee_754(0.0)

z0 = angle_degrees

for i in range(0, 129):
    if z0 > 0:
        x1 = ieee754_add(x0, exp_bin_str(y0,i))
        y1 = ieee754_add(y0, neg_bin_str(exp_bin_str(x0,i)))
        z1 = z0 - lookup_table[i]
    else:
        x1 = ieee754_add(x0, neg_bin_str(exp_bin_str(y0,i)))
        y1 = ieee754_add(y0, exp_bin_str(x0,i))
        z1 = z0 + lookup_table[i]
        
    x0 = x1
    y0 = y1
    z0 = z1
    
    print(f"\ni = {i} x1 = {x1} [{binary_ieee_754_to_float(x1)}] y1 = {y1} [{binary_ieee_754_to_float(y1)}] z1 = {z1}")
    
x = 0.6073 * binary_ieee_754_to_float(x1)
y = 0.6073 * binary_ieee_754_to_float(y1)

print(f"\n\ncos{angle_degrees} = {x} \nsin{angle_degrees} = {y}")
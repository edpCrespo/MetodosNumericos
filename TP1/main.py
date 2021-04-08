from numpy import nan, isnan, array, binary_repr

MAX = 2 ** 16
MIN = 2 ** -24
MIN_NORMAL = 2**-14
BIAS = 15

def dec2binf(num: float):
    # Nan
    if isnan(num):
        return array([0] + [1] * 15)

    abs_num = abs(num)
    sign_bit = int(num < 0)

    # Infinito o Cero
    if abs_num >= MAX:
        return array([sign_bit] + [1] * 5 + [0] * 10)
    elif abs_num < MIN:
        return array([sign_bit] + [0] * 15)

    # Normal o Sub-Normal
    if abs_num >= MIN_NORMAL:
        exp = 0
        if abs_num >= 2:
            while int(abs_num) > 1:
                abs_num /= 2
                exp += 1
        elif abs_num < 1:
            while int(abs_num) < 1:
                abs_num *= 2
                exp -= 1
        dec = abs_num - 1
    else:
        exp = -BIAS
        dec = abs_num
    mantissa = [0]*10

    for i in range(-1, -11, -1):
        exp_m = 2.0**i
        mantissa[-i-1] = int(not(exp_m > dec))
        if mantissa[-i-1]:
            dec -= exp_m

    return array([sign_bit] + list(map(int, list(binary_repr(exp + BIAS, 5)))) + mantissa)

print(dec2binf(19.88))

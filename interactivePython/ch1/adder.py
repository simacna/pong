from itertools import product

def and_gate(a, b):
    return a & b

def xor_gate(a, b):
    return a ^ b

def half_adder(a, b):
    sum_bit = xor_gate(a, b)
    carry_bit = and_gate(a, b)
    return carry_bit, sum_bit 

def full_adder(a, b, c):
    c0, s0 = half_adder(a, b)
    c1, s = half_adder(c, s0)
    c = xor_gate(c0, c1)
    return c, s

bits = (0, 1)



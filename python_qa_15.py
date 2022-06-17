# write a function called exponent(base,exp) that returns an int value of base raises to the power of exp.

base = 2
exp = 5
def exponent(base, exp):
    if exp == 1:
        return base
    else:
        return base * exponent(base, exp - 1)

    
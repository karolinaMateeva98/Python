def powersum(power, *args):
    '''Return the sum of each argument raised to the specified power.'''
    total = 0
    for i in args:
        total += pow(i, power)
    return total

powersum(2, 3, 4)
25
powersum(2, 10)
100
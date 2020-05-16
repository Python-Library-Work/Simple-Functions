# Yeah, that is a old repository of "functions"
# but, I may use for check how much I learned since I started
# programming. And how much I learned since my last post :)

def Split8 (Integer, Length=8, DisableBoolFlag=False):
    """
        Split a Integer to 8 bit format.
        The flag on [0] is the negative flag.
    """
    value =  -(Integer) if Integer < 0 else Integer
    buffer = []
    if DisableBoolFlag: buffer.append( 1 if Integer < 0 else 0 )
    else: buffer.append(Integer < 0)

    for i in range (0, Length):
        buffer.append(value & 0xFF)
        value = value >> 8

    return buffer

def Convert8 (List, Length=8):
    """
        Convert the Splited list of 8 bit numbers.
    """
    value   = 0
    b       = 0
    for i in range (0, Length):
        try:    value += (List[(i + 1)] << b)
        except: break
        b = b + 8

    if List[0] or List[0] != 0: value = -(value)
    return value


def test ():
    """
        Do some test on the internal functions
    """
    import random
    c = 0
    while c < 10:
        N = random.randint(-(1<<32), (1<<32))
        X = Split8 (N, DisableBoolFlag=True)
        Y = Convert8 (X)

        print("N = " + str(N) + " | X = " + str(X) + " | Y = " + str(Y) + " ? Match: " + str(N == Y))
        c += 1


if __name__ == '__main__':
    test()

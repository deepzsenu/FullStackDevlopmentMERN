def convert(value):
    binary = []
    negative = False

    if value < 0:
        negative = True
        value = abs(value)

    while value > 0:
        binary.append(value % 2)
        value //= 2

    while len(binary) < 16:
        binary.append(0)

    if negative:
        for i in range(len(binary)):
            binary[i] = 1 - binary[i]

        carry = 1
        for i in range(len(binary)):
            binary[i] += carry
            if binary[i] > 1:
                binary[i] = 0
            else:
                carry = 0

    binary.reverse()
    return ''.join(map(str, binary))

#test function

def test():
    # Test program for the convert function
    for value in [0, -1, 1, 63, 5000]:
        print(f"{value: 6d} {convert(value)}")


# calling test function
test()

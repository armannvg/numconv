
def findActiveBits(sequence):
    output = []
    location = 0;
    
    for c in reversed(str(sequence)):
        if c == '1':
            output.append(location)
        location += 1

    return str(output)

#Wrapper function to converting to binary, expects num parameter to be int
def convert(num, args=None):
    output = bin(num)[2:]

    if (args is not None) and args.show_active_bits:
        output = str(output) + " " + findActiveBits(output)

    return output
import roman

#Wrapper function to converting to roman numeral, expects num parameter to be int
def convert(num):
    try:
        return roman.to_roman(num)
    except roman.OutOfRangeError:
        return "Out of range"
    except roman.NotIntegerError:
        return "Not an integer"
    except roman.InvalidRomanNumeralError:
        return "Not a valid roman numeral"
    except Exception:
        return "Error during conversion"
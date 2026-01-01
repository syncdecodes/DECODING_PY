def analyze_ch(ch):
    ch = str(ch)
    if len(ch) != 1:
        return "invalid"

    ltrs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = "1234567890"

    if ch in ltrs:
        return "letter"
    elif ch in nums:
        return "number"
    else:
        return "special"

def case(char):
    char = str(char)
    if len(char) != 1:
        return "invalid"
    if analyze_ch(char) == "letter":
        return "Upper" if char.isupper() else "Lower"
    else:
        return "char is not a letter"

def num_name(n):
    n = str(n)
    if len(n) != 1: return "invalid"
    if n not in "1234567890": return "char is not a number"
    numbers = {'0': 'ZERO', '1': 'ONE', '2': 'TWO', '3': 'THREE', '4': 'FOUR',
            '5': 'FIVE', '6': 'SIX', '7': 'SEVEN', '8': 'EIGHT', '9': 'NINE'}
    return numbers[n]

def charcter_operation(character):
    print(analyze_ch(character))
    print(case(character))
    print(num_name(character))

charcter_operation("3")
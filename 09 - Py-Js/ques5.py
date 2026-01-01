def str_freq(string):
    freq = {}
    for ch in string:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    return freq

def replace_ch(string, Old, New):
    string = string.replace(Old, New)
    return string

def remove_first_ch(string, ch):
    index = string.find(ch)
    removed = string[:index] + string[index+1:]
    return removed
print(remove_first_ch("dev codes", "e"))

def remove_all_ch(string, ch):
    removed = string.replace(ch, "")
    return removed
print(remove_all_ch("dev codes", "e"))

def swap_ch(s4, s5, n):
    if n <= len(s4) and n <= len(s5):
        # swapping first n characters
        swapped_s4 = s5[:n] + s4[n:]
        swapped_s5 = s4[:n] + s5[n:]

        print("After swapping:")
        print("String 1:", swapped_s4)
        print("String 2:", swapped_s5)
    else:
        print("n is larger than the length of one of the strings!")


def to_int(in_string):
    out_num = 0
    if in_string[0] == "-":
        multiplier = -1
        in_string = in_string[1:]
    else:
        multiplier = 1
    
    for c in in_string:
        out_num = out_num * 10 + int(c)
    return out_num * multiplier

def to_string(in_int):
    out_str = ""
    prefix = ""
    if in_int < 0:
        prefix = "-"
        in_int = -in_int
    while in_int // 10 != 0:
        out_str = str(in_int % 10) + out_str
        in_int = in_int // 10
    out_str = str(in_int % 10) + out_str
    return prefix + out_str

print(to_string(2))
print(to_string(23445))
print(to_string(-23445))
print(to_int("14234"))
print(to_int("12345"))
print(to_int("-3512"))
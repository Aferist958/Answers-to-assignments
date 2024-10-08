def segment_numb(lst: list):
    out = []
    for i in range(lst[0], lst[1]+1):
        if str(i) in '1234567890' or str(i) in '0987654321':
            out.append(i)

    return out
print(segment_numb([100, 5000000000]))


from datetime import datetime
def random(lst: list):
    out = []
    while True:
        c = datetime.now()
        k = int(0 + (len(lst) - 1 - 0 + 1 - 10 ** -8) * c.microsecond / 1000000)
        if lst[k] not in out:
            out.append(lst[k])
        if out == lst:
            out = []
        if len(out) == len(lst):
            break
    return out
print(random([1,2,3,4,5]))
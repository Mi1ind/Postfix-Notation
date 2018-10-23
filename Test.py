val = 5
coords = ["21", "132", "645", "+", "-"]
el = coords
print(el)

val = 5 #number of digits and symbold in coords

i = 0
while i < val:
    if coords[i].isdigit():
        pass
    else:
        el[:i]
#        for val1 in coords[i]
#        print(coords[i])
i += 1
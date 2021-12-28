import re
import functools

def reducing_f(acc, curr):
    acc[0][0] = min(acc[0][0], curr[0])
    acc[0][1] = max(acc[0][1], curr[0])
    acc[1][0] = min(acc[1][0], curr[1])
    acc[1][1] = max(acc[1][1], curr[1])
    acc[2][0] = min(acc[2][0], curr[2])
    acc[2][1] = max(acc[2][1], curr[2])

    return acc

coordfilename = "coords.txt"
	
fin = open(coordfilename,'r')
coords_raw = fin.readlines()

coords_bits = [i.split(",") for i in coords_raw]

coords = []

for slab in coords_bits:
    new_coord = []
    for i in slab:
        new_coord.append(int(re.sub(r'[^-\d]','', i)))
    coords.append(new_coord)

result = functools.reduce(reducing_f, coords, [[1000, -1000], [1000, -1000], [1000, -1000]])

print(result)
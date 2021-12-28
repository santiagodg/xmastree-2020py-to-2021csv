# Turns 2021 GIFT coordinates file to 2020's coords.txt format and prints it to stdout.

import csv

with open('matts_coords_2021.csv', newline='') as f:
    reader = csv.reader(f)

    data = list(reader)

    data = list(map(lambda x: [float(x[0]), float(x[1]), float(x[2])], data))

    data = list(map(lambda x: [round((x[0] * 500) - 250), round((x[1] * 500) - 250), round((x[2] * 300) - 450)], data))

    data = list(map(lambda x: [str(x[0]), str(x[1]), str(x[2])], data))

    data = list(map(lambda x: "[" + ", ".join(x) + "]", data))

    print(*data, sep = "\n")

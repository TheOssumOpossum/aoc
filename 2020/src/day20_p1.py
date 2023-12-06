# https://adventofcode.com/2020/day/20

day = "20"

#part 1
txt = open("../../input/2020/day" + day + ".txt", "r")
# txt = open("../tst/day" + day + "_test.txt", "r")
txt = txt.readlines()
txt.append("\n")
result = 0

tiles = {}
tile_adjacencies = {}
borders = {}
current_tile = 0
for l in txt:
    if l == "\n":
        ''
        continue
    l = l.strip()
    if len(l) > 1 and l[0] == "T":
        l = l[5:-1]
        current_tile = int(l)
        tiles[current_tile] = []
        row = 0
    else:
        tiles[current_tile].append([])
        for c in l:
            tiles[current_tile][row].append(c)
        row += 1

def get_top(ls):
    return ''.join(ls[0])

def get_bottom(ls):
    return ''.join(ls[-1])

def get_right(ls):
    right = []
    for i in range(len(ls)):
        right.append(ls[i][-1])
    return ''.join(right)

def get_left(ls):
    left = []
    for i in range(len(ls)):
        left.append(ls[i][0])
    return ''.join(left)

for i in tiles:
    t = tiles[i]
    top = get_top(t)
    bot = get_bottom(t)
    r = get_right(t)
    l = get_left(t)
    top_r = top[::-1]
    bot_r = bot[::-1]
    r_r = r[::-1]
    l_r = l[::-1]

    if top in borders and borders[top] != i:
        match = borders[top]
        if i not in tile_adjacencies:
            tile_adjacencies[i] = []
        tile_adjacencies[i].append(match)
        if match not in tile_adjacencies:
            tile_adjacencies[match] = []
        tile_adjacencies[match].append(i)
    else:
        borders[top] = i

    if bot in borders and borders[bot] != i:
        match = borders[bot]
        if i not in tile_adjacencies:
            tile_adjacencies[i] = []
        tile_adjacencies[i].append(match)
        if match not in tile_adjacencies:
            tile_adjacencies[match] = []
        tile_adjacencies[match].append(i)
    else:
        borders[bot] = i

    if r in borders and borders[r] != i:
        match = borders[r]
        if i not in tile_adjacencies:
            tile_adjacencies[i] = []
        tile_adjacencies[i].append(match)
        if match not in tile_adjacencies:
            tile_adjacencies[match] = []
        tile_adjacencies[match].append(i)
    else:
        borders[r] = i

    if l in borders and borders[l] != i:
        match = borders[l]
        if i not in tile_adjacencies:
            tile_adjacencies[i] = []
        tile_adjacencies[i].append(match)
        if match not in tile_adjacencies:
            tile_adjacencies[match] = []
        tile_adjacencies[match].append(i)
    else:
        borders[l] = i

    if top_r in borders and borders[top_r] != i:
        match = borders[top_r]
        if i not in tile_adjacencies:
            tile_adjacencies[i] = []
        tile_adjacencies[i].append(match)
        if match not in tile_adjacencies:
            tile_adjacencies[match] = []
        tile_adjacencies[match].append(i)
    else:
        borders[top_r] = i

    if bot_r in borders and borders[bot_r] != i:
        match = borders[bot_r]
        if i not in tile_adjacencies:
            tile_adjacencies[i] = []
        tile_adjacencies[i].append(match)
        if match not in tile_adjacencies:
            tile_adjacencies[match] = []
        tile_adjacencies[match].append(i)
    else:
        borders[bot_r] = i

    if r_r in borders and borders[r_r] != i:
        match = borders[r_r]
        if i not in tile_adjacencies:
            tile_adjacencies[i] = []
        tile_adjacencies[i].append(match)
        if match not in tile_adjacencies:
            tile_adjacencies[match] = []
        tile_adjacencies[match].append(i)
    else:
        borders[r_r] = i

    if l_r in borders and borders[l_r] != i:
        match = borders[l_r]
        if i not in tile_adjacencies:
            tile_adjacencies[i] = []
        tile_adjacencies[i].append(match)
        if match not in tile_adjacencies:
            tile_adjacencies[match] = []
        tile_adjacencies[match].append(i)
    else:
        borders[l_r] = i

mult = 1
mults = 0
for t in tile_adjacencies:
    count = 0
    if len(tile_adjacencies[t]) == 4:
        mult *= t
        mults += 1
print(mult)

print(mults)

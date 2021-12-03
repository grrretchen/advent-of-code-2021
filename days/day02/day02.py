# generate a data set from a sample, or from a file. --------------------------
def sample(fpath):
    dataset = []

    with open(fpath, "r") as infile:
        for line in infile:
            # some of these lines might be blank, so skip those.
            try:
                dataset.append(line)
            except:
                continue

    print("Total records: %s"%len(dataset))
    return dataset


# parse the dataset into a list -----------------------------------------------
def parse(feed):
    # split this into a list of lists
    alpha = [a.strip().split(" ") for a in feed]

    # and list-comprehension to convert the second value into an int.
    beta = [[f[0], int(f[1]) if f[1] is type(int) else f[1]] for f in alpha]

    return beta


# determine the total offset along each vector (up, down, forward, back) ------
def pilot(path):
    position = {}
    for point in path:
        if len(point) != 2:
            continue
        if not point[0] in position:
            position[point[0]] = 0
        position[point[0]] += int(point[1])

    return(position)


# find the true h and true v offset, for a final endpoint. --------------------
def endpoint(delta):
    for mode in ['up', 'down', 'forward', 'back']:
        if not mode in delta:
            delta[mode] = 0
    
    v = delta['down'] - delta['up']
    h = delta['forward'] - delta['back']

    return {"h" : h, "v": v}


# for part 2, we need to multiply the vertical aim by the horizontal movement. -
def aim(frameset):
    aim = 0
    h = 0
    d = 0
    for point in frameset:
        if len(point) != 2:
            continue
        if point[0] in ['up', 'down']:
            # the aim is a rolling sum of previous up/down movements.
            aim += int(point[1]) if point[0] == 'down' else int(point[1])*-1
        if point[0] == "forward":
            d += int(point[1]) * aim
            h += int(point[1])

    return {"h" : h, "v" : d}


# do the main -----------------------------------------------------------------
def main():
    # fpath = "./day02-sample.txt" # this is the sample dataset.
    fpath = "./day02-data.txt"
    dataset = sample(fpath)
    frameset = parse(dataset)
    delta = pilot(frameset)
    pos_p1 = endpoint(delta)
    part1 = pos_p1["h"] * pos_p1["v"]
    print(part1)


    pos_p2 = aim(frameset)
    part2 = pos_p2["h"] * pos_p2["v"]
    print(part2)
    # return result

# =============================================================================
if __name__ == "__main__" :
    result = main()
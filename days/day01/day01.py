#!/usr/bin/env python3


# generate a data set from a sample, or from a file.
def sample(fpath):
    dataset = []

    with open(fpath, "r") as infile:
        for line in infile:
            # some of these lines might be blank or non-int, so skip those.
            try:
                dataset.append(int(line))
            except:
                continue

    print("Total records: %s"%len(dataset))
    return dataset


# make a dataset which is a rolling sum of every (x) records.
def frames(dataset = [], framesize = 3):
    frameset = []
    r = [0]*framesize

    for i in range(len(dataset)):
        for j in range(framesize):
            # use the modulo to determine which r[index] to use.
            r[j] = dataset[i] if i%framesize == j else r[j]
        if i < framesize:
            # skip the first (framesize) records until the full array is loaded.
            continue
        if i <= len(dataset):
            # sum the entire array for each frame.
            frameset.append(sum(r))
    
    print("Total frames: %s"%len(frameset))
    return frameset


# determine records which are greater than the previous record.
def depths(frameset=[]):

    incr = 0
    decr = 0
    last = None

    for this in frameset:
        if not last:
            last = this
            continue
        if last < this:
            incr +=1
        elif last > this:
            decr += 1
        last = this

    print("Total increases: %s"%incr)
    return incr


# do the main.
def main():
    fpath = "./sample.txt" # this is the sample dataset.
    fpath = "./data.txt"
    dataset = sample(fpath)
    frameset = frames(dataset, framesize=3)
    depthset = depths(frameset)

    result = {
        "records" : len(dataset),
        "frames" : len(frameset),
        "depths" : depthset
    }
    return result


# =============================================================================
if __name__ == "__main__" :
    result = main()
    print(result)

import re


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

    result = [a.strip() for a in dataset]
    return result


# parse the dataset into a list -----------------------------------------------
def parse(dataset):
    # clean up the list, and init an array for the length of the string.
    len_ds = len(dataset)
    beta = [0] * len(dataset[0])
    
    # step through each character, add the integer value blindly to the array.    
    for row in dataset:
    	for bit in range(len(row)):
    		beta[bit] += int(row[bit])
        
    # divide the sum of each value by the total record count, and round up/down.
    g_bin = [round(i/len_ds) for i in beta]
    # then, do fancy math to find the inverse.
    e_bin = [1-i for i in g_bin]
    
    # also calc as a percentage, which we'll use for regex patterns
    g_pct = [i/len_ds for i in beta]
    e_pct = [(len_ds-i)/len_ds for i in beta]
    
    # seed a list for regex pattern matching
    e_re = e_bin.copy()
    g_re = g_bin.copy()

    # do special rules on the regex pattern when a value occurs exactly 50%
    for i in range(len(g_re)):
        e_re[i] = "0" if e_pct[i] == 0.5 else e_re[i]
        g_re[i] = "1" if g_pct[i] == 0.5 else g_re[i]

    # then collapse the regex list into a stingle string
    e_re = "".join([str(i) for i in e_re])
    g_re = "".join([str(i) for i in g_re])

    # send it home.
    result = {
    	"g_bin" : g_bin,
    	"e_bin" : e_bin,
        "g_pct" : g_pct,
        "e_pct" : e_pct,
        "g_re" : g_re,
        "e_re" : e_re,
    	}

    return result


# parse the dataset into a list -----------------------------------------------
def part1(e = [], g = []):
    # collapse the list into a single string.
	e_str = "".join([str(i) for i in e])
	g_str = "".join([str(j) for j in g])
	
    # convert the string-coded binary into an integer
	e_bin = int(e_str, 2)
	g_bin = int(g_str, 2)
	
	result = e_bin * g_bin
	return result


# we need to slowly, recursively reduce the dataset until we have a match.
def reduce(pattern, dataset, bs_type="g_re"):
    # seed a list to store each bit per criteria
    tumbler = ['0'] * len(pattern)

    # we'll slowly step through the dataset, position by position.
    for i in range(len(pattern)):
        j = i+1

        # parse the payload and set the tumbler to the corresponding bit
        bitset = parse(dataset)
        pattern=bitset[bs_type]
        tumbler[i] = str(pattern[i])

        # set a regex based on the tumbler, plus a wildcard to pad the string.
        bite = f"{''.join(tumbler[0:j])}\d{{{len(pattern)-j}}}"
        _dataset = re.findall(f"({bite})", f"|{'|'.join(dataset)}|")

        # if we find a perfect match, then send it home.            
        if len(_dataset) == 1:
            return _dataset[0]

        # otherwise, send the current values forward and loop again.
        last = bite
        dataset = _dataset


# parse the dataset into a list -----------------------------------------------
def part2(pattern = [], dataset = []):    
    # send a copy of the each dataset to the reducer.
    g = reduce(pattern["g_re"], dataset.copy(), bs_type="g_re")
    e = reduce(pattern["e_re"], dataset.copy(), bs_type="e_re")

    # remap the string-binary into an integer.
    e_result = int(e,2)
    g_result = int(g,2)

    result = {
        "O2" : g_result,                 # g is a measurement of O2
        "CO2" : e_result,                # e is a measurement of CO2
        "product" : g_result * e_result
    }

    return result


# do the main -----------------------------------------------------------------
def main():
    # fpath = "./day03-sample.txt" # this is the sample dataset.
    fpath = "./day03-data.txt"
    dataset = sample(fpath)
    print("Total records: %s"%len(dataset))

    bitset = parse(dataset)
    print(f"Register values: {bitset}")

    part1final = part1(e = bitset["e_bin"], g = bitset["g_bin"])
    print(f"Part 1 result: {part1final}")

    part2final = part2(pattern = bitset, dataset = dataset)
    print(f"Part 2 result: {part2final}")


# =============================================================================
if __name__ == "__main__" :
    result = main()

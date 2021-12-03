import urllib.request as request

def download():
	
    request.urlretrieve("https://adventofcode.com/2021/day/3/input", "day03-data.txt")



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
    alpha = [a.strip() for a in feed]
    beta = [0] * len(alpha[0])
    
    for row in alpha:
    	for bit in range(len(row)):
    		beta[bit] += int(row[bit])
    
    print(beta)
    
    gamma = [round(i/len(alpha)) for i in beta]
    epsilon = [1-i for i in gamma]
    print(gamma)
    print(epsilon)
    
    result = {
    	"gamma" : gamma,
    	"epsilon" : epsilon
    	}
    return result

def part1(e = [], g = []):
	e_str = "".join([str(i) for i in e])
	g_str = "".join([str(j) for j in g])
	print(e_str)
	print(g_str)
	
	e_bin = int(e_str, 2)
	g_bin = int(g_str, 2)
	
	result = e_bin * g_bin
	print(result)
	return result


# do the main -----------------------------------------------------------------
def main():
    #fpath = "./day03-sample.txt" # this is the sample dataset.
    fpath = "./day03-data.txt"
    dataset = sample(fpath)
    bitset = parse(dataset)
    part1final = part1(e = bitset["epsilon"], g = bitset["gamma"])
    #print(part1)


    #pos_p2 = aim(frameset)
    #part2 = pos_p2["h"] * pos_p2["v"]
    #print(part2)
    # return result

# =============================================================================
if __name__ == "__main__" :
    result = main()

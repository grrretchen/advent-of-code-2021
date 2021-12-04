

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



# do the main -----------------------------------------------------------------
def main():
    # fpath = "./day03-sample.txt" # this is the sample dataset.
    fpath = "./day03-data.txt"
    dataset = sample(fpath)


# =============================================================================
if __name__ == "__main__" :
    result = main()

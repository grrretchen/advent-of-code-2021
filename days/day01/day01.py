#!/usr/bin/env python3

class Problem:
  def __init__(self,dataset):
    self.result1 = None
    self.result2 = None
    self.dataset = self.parse(dataset)


  # ------------------------------------------------------------------------
  def parse(self, dataset):
    result = [int(x) for x in dataset]
    return result


  # ------------------------------------------------------------------------
  def compare(self,data):
    last = data[0]
    result = 0
    for row in data[1:]:
      if row>last:
        result +=1
      last = row
    return result


  # ------------------------------------------------------------------------
  def part1(self):
    self.result1 = self.compare(self.dataset)
    return(self.result1)


  # ------------------------------------------------------------------------
  def part2(self):
    frames = []
    for i in range(0,len(self.dataset)-2):
      frames.append(sum(self.dataset[i:i+3]))

    self.result2 = self.compare(frames)

    return(self.result2)


# --------------------------------------------------------------------------
# pull the dataset from a file 
def fetch(fpath):
  dataset = []
  
  with open(fpath, "r") as infile:
    dataset = [line.strip("\n\r") for line in infile.readlines()]
        
  return dataset


# --------------------------------------------------------------------------  
# solve the problems.
def solve(dataset):
  p = Problem(dataset)

  p.part1()
  p.part2()

  return (p.result1, p.result2)  


# --------------------------------------------------------------------------
# do the main 
def main():
  fpath = "./sample.txt" # this is the sample dataset.
  fpath = "./data.txt"
  dataset = fetch(fpath)
  
  r1,r2 = solve(dataset)

  result = {
    "Part 1" : r1,
    "Part 2" : r2
  }

  return result


# ==========================================================================
if __name__ == "__main__" :
  result = main()
  print(result)

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
def test():
  # TEST, and exit if failure
  fpath = "./test.txt" # this is the sample dataset.

  try:
    P = Problem(fetch(fpath))
    assert 7 == P.part1()
  except AssertionError as e:
    print("Assertion Error in Part 1")
    return False

  try:
    P = Problem(fetch(fpath))
    assert 5 == P.part2()
  except AssertionError as e:
    print("Assertion Error in Part 2")
    return False

  return True


# --------------------------------------------------------------------------
# do the main 
def main():


  # RUN
  try:
    fpath = "./data.txt" # this is the sample dataset.
    P = Problem(fetch(fpath))
    result1 = P.part1()
    result2 = P.part2()
  except Exception as e:
    print(e)


  result = {
    "Part 1" : result1,
    "Part 2" : result2
  }

  return result


# ==========================================================================
if __name__ == "__main__" :
  if not test():
    exit()

  result = main()
  print(result)

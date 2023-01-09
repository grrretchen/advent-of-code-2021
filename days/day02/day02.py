class Problem:
  def __init__(self,dataset):
    self.result1 = None
    self.result2 = None
    self.dataset = self.parse(dataset)


  # ------------------------------------------------------------------------
  # parse the dataset into a list -----------------------------------------------
  def parse(self, data):
      # split this into a list of lists
      alpha = [a.strip().split(" ") for a in data]

      # and list-comprehension to convert the second value into an int.
      beta = [[f[0], int(f[1]) if f[1] is type(int) else f[1]] for f in alpha]

      return beta  

  # ------------------------------------------------------------------------
  def part1(self):
    path = {
      'forward':0,
      'up':0,
      'down':0
      }

    for row in self.dataset:
      path[row[0]]+= int(row[1])

    h = path['forward']
    v = path['down'] - path['up']

    print("h: %s\t v: %s"%(h,v))
    self.result1 = h*v
    return(self.result1)


  # ------------------------------------------------------------------------
  # for part 2, we need to multiply the vertical aim by the horizontal movement. -
  def part2(self):
    aim = 0
    h = 0
    v = 0
    for point in self.dataset:
        if len(point) != 2:
            continue
        if point[0] in ['up', 'down']:
            # the aim is a rolling sum of previous up/down movements.
            aim += int(point[1]) if point[0] == 'down' else int(point[1])*-1
        if point[0] == "forward":
            v += int(point[1]) * aim
            h += int(point[1])

    print("h: %s\t v: %s"%(h,v))
    self.result2 = h*v
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
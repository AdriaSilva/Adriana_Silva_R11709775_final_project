# Adriana Silva R11709775 CS-3361-002 Date: 12/2/2022
import argparse
from multiprocessing import Pool

parser = argparse.ArgumentParser(description='cellular life simulator')

parser.add_argument('-i', type=str, required = True)
parser.add_argument('-o', type=str, required = True)
parser.add_argument('-t', type=int, default=1)

args = parser.parse_args()
#print(args)

print("Project :: R11709775")

def prime(n):
  x = 1
  start = 2
  if (n == 0 or n == 1):
    x = 0
  else:
    for i in range(n - 2):
      if (n % start == 0):
        x = 0
  return x

def changing_rows(rows):
  row = rows[0]
  row_index = rows[1]
  matrix = rows[2]

  new_matrix = [r[:] for r in matrix]

  y = 0
  for _ in range(len(row)-1):
    if(row[y] == '+'):
      living_neigbours = 0
      if(y == 0):
        q = -1
      else:
        q = 0
      if(y==len(row)-2):
        p = 1
      else:
        p = 0
              
      if (matrix[row_index - 1][y - 1+q] == '+'):
        living_neigbours = living_neigbours + 1
      if (matrix[row_index - 1][y] == '+'):
        living_neigbours = living_neigbours + 1
      if (matrix[row_index - 1][y - (len(row)-1)+p] == '+'):
        living_neigbours = living_neigbours + 1
      if (matrix[row_index][y - 1+q] == '+'):                
        living_neigbours = living_neigbours + 1
      if (matrix[row_index][y - (len(row)-1)+p] == '+'):
        living_neigbours = living_neigbours + 1
      if (matrix[row_index - (len(matrix)-1)][y - 1+q] == '+'):
        living_neigbours = living_neigbours + 1
      if (matrix[row_index - (len(matrix)-1)][y] == '+'):
        living_neigbours = living_neigbours + 1
      if (matrix[row_index - (len(matrix)-1)][y - (len(row)-1)+p] == '+'):
        living_neigbours = living_neigbours + 1

      if (living_neigbours == 2 or living_neigbours == 4 or living_neigbours == 6):
        new_matrix[row_index][y] = '+'
      else:
          new_matrix[row_index][y] = '-'
    else:
      if(row[y] == '-'):
        living_neigbours = 0
        if(y == 0):
          q = -1
        else:
          q = 0
        if(y==len(row)-2):
          p = 1
        else:
          p = 0
              
        if (matrix[row_index - 1][y - 1+q] == '+'):
          living_neigbours = living_neigbours + 1
        if (matrix[row_index - 1][y] == '+'):
          living_neigbours = living_neigbours + 1
        if (matrix[row_index - 1][y - (len(row)-1)+p] == '+'):
          living_neigbours = living_neigbours + 1
        if (matrix[row_index][y - 1+q] == '+'):                
          living_neigbours = living_neigbours + 1
        if (matrix[row_index][y - (len(row)-1)+p] == '+'):
          living_neigbours = living_neigbours + 1
        if (matrix[row_index - (len(matrix)-1)][y - 1+q] == '+'):
          living_neigbours = living_neigbours + 1
        if (matrix[row_index - (len(matrix)-1)][y] == '+'):
          living_neigbours = living_neigbours + 1
        if (matrix[row_index - (len(matrix)-1)][y - (len(row)-1)+p] == '+'):
          living_neigbours = living_neigbours + 1

        p = prime(living_neigbours)
        if (p == 1):
          new_matrix[row_index][y] = '+'
        else:
          new_matrix[row_index][y] = '-'
        
    
    y += 1
  return new_matrix[row_index]

def simulator(matrix, T):
  for i in range(100):
    rows = []
    num = 0
    for _ in range(len(matrix)):
      r = [matrix[num], num, matrix]
      rows.append(r)
      num += 1
      
    final_matrix = [row[:] for row in matrix]
    
    new_rows = []
    
    with Pool(T) as pool:
      new_rows = pool.map(changing_rows, rows)
      r_in = 0
      for n_row in new_rows:
        final_matrix[r_in] = new_rows[r_in]
        r_in += 1
    
    matrix = [row[:] for row in final_matrix]
  del(final_matrix[len(final_matrix)-1][len(final_matrix[0])-1])
  return final_matrix


def main():
  inputFile = open(args.i, "r")
  T = args.t
  matrix = []

  for x in inputFile:
    if len(x)>1:
      row2 = []
      row2[:] = x
      matrix.append(row2)

  ROW = len(matrix)
  COLUMN = len(matrix[0])

  if(len(matrix[ROW-1])!=COLUMN):
    matrix[ROW-1].append("\n")

  final_matrix = simulator(matrix, T)

  outputFile = open(args.o, "w")

  
  index = 0
  for i in range(ROW):
    ind = 0
    for x in range(len(final_matrix[index])):
      outputFile.write(final_matrix[index][ind])
      ind = ind + 1
    index = index + 1

  inputFile.close()
  outputFile.close()



main()

from algo1 import *
from algo2 import *
import matplotlib.pyplot as plt


def clique_generate(size):
  list = range(1,size+1)
  matrix = []
  for i in range(1, size+1):
    for j in range(1, i):
      add_text = str(i)+"\t"+str(j)
      matrix.append(add_text)
  return matrix
      


def algo1_time(size):
  matrix = clique_generate(size)
  graph = algo1_graph([],[])
  graph.generate(matrix)
  graph.show()
  optgraph, optdensity, time = graph.finding_densest_subgraph()
  return time
  
def plot_generate(size):
  x = range(2, size+1)
  y = [algo1_time(k) for k in x]
  
  plt.plot(x, y)
  
  plt.xlabel('x - axis')
  plt.ylabel('y - axis')
  
  plt.title('Time Complexity Analysis')
  
  plt.show()

if __name__ == "__main__":
	
  print("time:", algo1_time(30))
  
  plot_generate(100)
	

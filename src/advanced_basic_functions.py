from dataclasses import dataclass, field
from typing import List
import time
import matplotlib.pyplot as plt

#construct dataclass "graph" with vertice and edges matrix
class graph:
    vertice: List[int] 
    matrix : List[str]
    degreetable: List[List[int]]
    neighbortable: List[List[int]]
    
    def __init__(self, matrix: List[str]):
      size1 = size(matrix)
      self.vertice = list(range(1, size1+1))
      self.degreetable = [[]]
      self.neighbortable = [[]]

    def generate(self, matrix):
      size1 = size(matrix)
      self.vertice = list(range(1, size1+1))
      
      neighbortable = rep(size1)
      #neighbortable = neighbortable1[:]      
      for s in matrix:
        s1, s2 = identity(s)
        neighbortable[s1].append(s2)
        neighbortable[s2].append(s1)
      self.neighbortable = neighbortable
      print("negihbortable:",neighbortable)
      
      degreetable= rep(size1)
      #degreetable = degreetable1[:]
      for v in self.vertice:
        vdegree = len(neighbortable[v])
        degreetable[vdegree].append(v)
      self.degreetable = degreetable
      print("degreetable:", degreetable)
      
    def show(self):
      print("The vertice are: \n{}\nand degreelist is:{}"
             .format(self.vertice, self.neighbortable))
             
    
    def degree(self, vertex):
      return len(degreetable[vertex])
      
    def update(self):
      
      #declare
      neighbortable = self.neighbortable
      degreetable = self.degreetable
            
      
      #removed vertex v
      vdegree = degreetable.index(next(filter(lambda x: len(x)!=0, degreetable)))
      v = degreetable[vdegree][0]
      vneighbor = neighbortable[v]
      
      #vertice update
      vertice_new = self.vertice     
      vertice_new.remove(v)
      self.vertice = vertice_new
      
      #degreetable update
      #vneighbor = neighbortable[v]
      #v10 = neighbortable[10]
      for n in vneighbor:
        ndegree = len(neighbortable[n])
        degreetable[ndegree].remove(n)
        degreetable[ndegree-1].append(n)
      degreetable[len(vneighbor)].remove(v)
           
      #neighbortable update
      vneighbor = neighbortable[v]
      for n in vneighbor:
        neighbortable[n].remove(v)
      neighbortable[v].clear()
      
      
    def density(self):
      edge = 0.0
      for vneighbor in self.neighbortable:
        edge += len(vneighbor)
      return edge/(2*len(self.vertice))
      
    def copy(self, second):
      second.vertice = self.vertice[:]
      second.neighbortable = self.neighbortable[:]
      second.degreetable = self.degreetable[:]
      
      
    def finding(self):
      optgraph = graph(["1 2"])
      self.copy(optgraph)
      density = optgraph.density()
      while len(self.vertice)>=2:
       
        self.update()
            
        currentdensity = self.density()
        
        if currentdensity > density:
           self.copy(optgraph)
           density = optgraph.density()
        
      print("optimal density is:", density)
      optgraph.show()
    
#calculate the size of graph over matrix
def size(matrix):
  datalist = []
  for edge in matrix:
    newtwo = edge.split(" ")
    datalist += newtwo
    
  datalist1 = [int(x) for x in datalist]
  
  return max(datalist1)
  
def rep(s):
  k = [[]]
  for i in range(1, s+3):
    k.append([])
  return k
    
    
  
def identity(s):
  newtwo =s.split(" ")
  return int(newtwo[0]), int(newtwo[1])
  
 
 
def clique_generate(size2):
  list = range(1,size2+1)
  matrix = []
  for i in range(1, size2+1):
    for j in range(1, i):
      add_text = str(i)+" "+str(j)
      matrix.append(add_text)
  return matrix
      


def algo1_time(size2):
  matrix = clique_generate(size2)
  graph1 = graph(["1 2"])
  graph1.generate(matrix)
  graph1.show()
  s1 = time.time()
  graph1.finding()
  s2 = time.time()
  return s2-s1
  
def plot_generate(size2):
  x = range(2, size2+1)
  y = [algo1_time(k) for k in x]
  
  plt.plot(x, y)
  
  plt.xlabel('x - axis')
  plt.ylabel('y - axis')
  
  plt.title('Time Complexity Analysis')
  
  plt.show()
 
  
#main function as we test
if __name__ == "__main__":
  f= open("class_example_undirected.txt","r")
  #f= open("data.txt","r")
  string = f.read()
  matrix = string.split("\n")
  del(matrix[-1])
  
  test = graph(matrix)
  test.generate(matrix)
  
  print("time:", algo1_time(10))
  
  plot_generate(300)
  '''
  print("1")
  test.show()
  test.update()
  print("2")
  test.show()
  '''
  

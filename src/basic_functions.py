from dataclasses import dataclass, field
from typing import List


#construct dataclass "graph" with vertice and edges matrix
class graph:
    vertice: List[int] 
    matrix : List[str]
    
    def __init__(self, vertice: List[int], matrix: List[str]):
      self.vertice = vertice
      self.matrix  = matrix

    def generate(self, matrix):
      self.vertice = list(range(1, int(size(matrix))+1))
      self.matrix  = matrix
      
    def show(self):
      print("The vertice are: \n{}\nand matrix is:{}"
             .format(self.vertice, self.matrix))
             
    
    def degree(self, vertex):
      if vertex not in self.vertice:
        print("The vertex you choose to get degree doesn't belong to the graph, please input another one!")
      matrix = self.matrix
      number = 0.0
      for edge in matrix:
        if str(vertex) in edge:
          number+=1
      if (number/2).is_integer() == False:
        print("WARNING: this graph might be directed because {} has number:{}".format(vertex, number))
      return number//2
  
  
	#update matrix by removing vertex and its edges
    def edgeupdate(self, vertex):
      matrix_new  = [edge for edge in self.matrix if str(vertex) not in edge]
      vertice_new = self.vertice
      
      vertice_new.remove(vertex)
      
      graph_new = graph(vertice_new, matrix_new)
      return graph_new


	   
	   
	#calculate the vertex with minimal degree   
    def minivertex(self):
      minidegree = 0
      minivertex = 0
      
      for i in self.vertice:
        if i == min(self.vertice):
          minidegree = self.degree(i)
          minivertex = min(self.vertice)
        else:
          currentdegree = self.degree(i)
          if currentdegree < minidegree:
            minidegree = currentdegree
            minivertex = i
      #print("minivertex: {} and its minidegree is: {}".format(minivertex,minidegree))
      if minivertex == 0:
        print("WARNING: The matrix might be empty")
      return minivertex

	  
	#complete iteration of every removal in both algo1 and algo2
    def iteration(self):
      remove_vertex = self.minivertex()
      new_graph = self.edgeupdate(remove_vertex)
      return new_graph
	 
	 
#calculate the size of graph over matrix
def size(matrix):
  datalist = []
  for edge in matrix:
    newtwo = edge.split("\t")
    datalist += newtwo
    
  datalist1 = [int(x) for x in datalist]
  
  return max(datalist1)
  
  
  
#main function as we test
if __name__ == "__main__":
  f= open("class_example.txt","r")
  #f= open("data.txt","r")
  string = f.read()
  matrix = string.split("\n")
  del(matrix[-1])
  
  new = graph([], [])
  new.generate(matrix)
  new.show()
  
  new2 = graph([0], ["0"])
  new2 = new
  #new2.show()
  
  print("degree of 4 is: ", new.degree(4))
  
  #print("edgeupdate:\n")
  #new = new.edgeupdate(4)
  #new.show()
  
  print("minivertex\n")
  v = new.minivertex()
  
  new = new.iteration()
  print("iter:\n")
  new.show()
  
  
  
  
  
  
  '''
 
  print("sdfgsfd:",matrix)
  
  print("size is:" + size(matrix))
  
  print("first outcome:", minivertex(matrix))
  
  print("first iteration:", iteration(matrix))
  
  '''

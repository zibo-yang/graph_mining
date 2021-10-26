from dataclasses import dataclass, field
from typing import List
from basic_functions import graph
import time



class algo2_graph(graph):
   
     def __init__(self, vertice: List[int], matrix: List[str]):
       super().__init__(vertice, matrix)
       
       
     #we calculate average density
     def average_density(self):
       edge_number = (len(self.matrix))
       vertex_number = len(self.vertice)

       return edge_number/vertex_number
    
      
      
     #finding densest graph with average density
     def finding_densest_subgraph(self):
       vertex_number = len(self.vertice)
  
       v = self.vertice[:]
       m = self.matrix[:]
       optimal_graph = algo2_graph(v, m)
       new_graph = algo2_graph(self.vertice, self.matrix)

       optimal_density = optimal_graph.average_density()
  
       for i in range(2, vertex_number):
      
         new_graph1 = new_graph.iteration()
         
         new_graph = algo2_graph(new_graph1.vertice, new_graph1.matrix)
         
         new_density = new_graph.average_density()
         
         
         if new_density > optimal_density:
           
           optimal_density = new_density
           optimal_graph.vertice = new_graph.vertice[:]
           optimal_graph.matrix = new_graph.matrix[:]
         
         
       print("optimal graph with optimal density {} is : ".format(optimal_density))
       optimal_graph.show()
       
       return optimal_graph, optimal_density
      
      
      
if __name__ == "__main__":
  f= open("class_example.txt","r")
  #f= open("data.txt","r")
  string = f.read()
  matrix = string.split("\n")
  del(matrix[-1])
  
  new = algo2_graph([],[])
  new.generate(matrix)
  new.show()
  
  start = time.time()
  
  opt, den = new.finding_densest_subgraph()
  end = time.time()
  
  print("calculation time is {}".format(end - start))

from dataclasses import dataclass, field
from typing import List
from basic_functions import graph
import time



class algo1_graph(graph):
   
     def __init__(self, vertice: List[int], matrix: List[str]):
       super().__init__(vertice, matrix)
       
       
     #we calculate clique density
     def clique_density(self):
       edge_number = (len(self.matrix))
       vertex_number = len(self.vertice)
       complete_clique = vertex_number * (vertex_number - 1) / 2
       return edge_number/complete_clique
    
      
      
     #finding densest graph with clique density
     def finding_densest_subgraph(self):
       start = time.time()
       vertex_number = len(self.vertice)
  
       v = self.vertice[:]
       m = self.matrix[:]
       optimal_graph = algo1_graph(v, m)
       new_graph = algo1_graph(self.vertice, self.matrix)

       optimal_density = optimal_graph.clique_density()
  
       for i in range(2, vertex_number):
      
         new_graph1 = new_graph.iteration()
         
         new_graph = algo1_graph(new_graph1.vertice, new_graph1.matrix)
         
         new_density = new_graph.clique_density()
         
         
         if new_density > optimal_density:
           
           optimal_density = new_density
           optimal_graph.vertice = new_graph.vertice[:]
           optimal_graph.matrix = new_graph.matrix[:]
         
         
       print("optimal graph with optimal density {} is : ".format(optimal_density))
       optimal_graph.show()
       end = time.time()
       print("calculation time is {}".format(end-start))
       return optimal_graph, optimal_density, (end-start)
      
      
      
if __name__ == "__main__":
  #f= open("class_example.txt","r")
  f= open("twin_city.txt","r")
  string = f.read()
  matrix = string.split("\n")
  del(matrix[-1])
  
  new = algo1_graph([],[])
  new.generate(matrix)
  new.show()
  
  
  
  opt, den, time = new.finding_densest_subgraph()
  
  

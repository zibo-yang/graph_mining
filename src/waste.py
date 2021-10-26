'''
	  for i in range(1, int(size(matrix))):
		if i == 1:
		  minidegree = degree(str(i), matrix)
		  minivertex = 1
		else:
		  currentdegree = degree(str(i), matrix)
		  if currentdegree < minidegree:
		    minidegree = currentdegree
		    minivertex = i
	  print("minivertex: {} and its minidegree is: {}"
		     .format(minivertex,minidegree))
	  if minivertex == 0:
		print("WARNING: The matrix might be empty")
	  return minivertex
	  '''
	  
	  '''
	  remove_vertex = minivertex(matrix)
	  new_matrix = edgeupdate(str(remove_vertex), matrix)
	  return new_matrix
	'''
	 '''
	def degree(self, vertex):
	  if vertex not in self.vertice:
	    print("The vertex you choose to get degree doesn't belong to the graph, please input another one!")
	  matrix = self.matrix
	  number = 0.0
	  for edge in matrix:
	    if str(vertex) in edge:
	      number+=1
	  if (number/2).is_integer() == False:
	    print("WARNING: this graph might be directed")
	  return number//2
	  '''

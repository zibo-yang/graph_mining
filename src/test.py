from dataclasses import dataclass, field
from typing import List
from basic_functions import graph


class test:

    k: List[int]

    
    def __init__(self, bg):
      self.k = bg
    
    
    def show(self):
      print("test.k:",self.k)
      
    def test1(self):
      k1 = self.k
      sn = test(k1)
      sb = test(self.k)
      
      sb.k.append(7)
      sn.show()
      sb.show()
      self.show()


if __name__ == "__main__":
    
    nb = test([8])
    nb.test1()
    
    print("5234")
    a = [1,2,3]
    b = a[:]
    c = a
    c.append(4)
    print(a)
    print(b)
    print(c)

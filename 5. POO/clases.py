class Punto:
   def __init__(self, x=0, y=0):
       self.x = x
       self.y = y   
   def imprimir(self):
        return print(f'({self.x},{self.y})')
   def suma(self,p2):
       x2 = self.x + p2.x
       y2 = self.y + p2.y
       return Punto(x2,y2)
   def colinealidad(self,p1,p2):
       a = self.x*(p1.y-p2.y)-self.y*(p1.x-p2.x)+(p1.x*p2.y-p1.y*p2.x)
       if a == 0:
           return print('son colineales')
       else:
           return print('no lo son')
       
"""   
p = Punto(1, 5)    
print(p)
p1 = Punto(2,6)
y=p.suma(p1)
y.imprimir()

p3= Punto(1)
p3.imprimir()
"""
p = Punto(5,1)
p1 = Punto(2,2)
p2 = Punto(-1,-1)
p.colinealidad(p1,p2)
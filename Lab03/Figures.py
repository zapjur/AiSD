#Figures
import math

class Circle:
    radius = 0

    def __init__(self,r):
        self.radius = r

    def __del__(self):
        pass
    
    def surface(self):
        return(math.pi*pow(self.radius,2))
    
    def circuit(self):
        return(2*math.pi*self.radius)

class Triangle:
    a = 0
    b = 0
    c = 0

    def __init__(self,ai,bi,ci):
        self.a = ai
        self.b = bi
        self.c = ci

    def __del__(self):
        pass

    def checkIfCorrect(self):
        x = max(self.a, self.b, self.c)
        sumEdges = self.a + self.b + self.c
        if sumEdges <= 2 * x:
            return False
        else:
            return True
    
    def setEdges(self, ai, bi, ci):
        self.a = ai
        self.b = bi
        self.c = ci

    def surface(self):
        circ = self.circuit()
        return(math.sqrt(circ*(circ-self.a)*(circ-self.b)*(circ-self.c)))
    
    def circuit(self):
        return(self.a+self.b+self.c)

class Square:
    a = 0

    def __init__(self,ai):
        self.a = ai

    def __del__(self):
        pass
    
    def surface(self):
        return(pow(self.a,2))
    
    def circuit(self):
        return(4*self.a)

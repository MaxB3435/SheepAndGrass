WHITE = color(255)
BROWN = color(102,51,0)
RED = color(255,0,0)
GREEN = color(0,102,0)
YELLOW = color(255,255,0)
PURPLE = color(102,0,204)




class Sheep:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.sz = 10 #size
        self.energy = 200
        
    
    def update(self):
        move = 1
        self.energy -= 1
        if self.energy <= 0:
            sheepList.remove(self)
        self.x += random(-move, move)
        self.y += random(-move, move)
        fill(WHITE)
        ellipse(self.x,self.y,self.sz,self.sz)
        

  
    
      
        
          
sheepList = []
        
                    
        
def setup():
    size(600,600)
    for i in range(3):
        sheepList.append(Sheep(random(width),
                               random(height)))
    
    
def draw():
    background(255)
    for sheep in sheepList:
        sheep.update()

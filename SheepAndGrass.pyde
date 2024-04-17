class Sheep:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.sz = 10 #size
        self.energy = 20
        
    
    def update(self):
        move = 1
        self.energy -= 1
        if sheep.energy <= 0:
            sheepList.remove(self)
        self.x += random(-move, move)
        self.y += random(-move, move)
        fill(255)
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

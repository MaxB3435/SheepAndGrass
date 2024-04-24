from random import choice
WHITE = color(255)
BROWN = color(102,51,0)
RED = color(255,0,0)
GREEN = color(0,102,0)
YELLOW = color(255,255,0)
PURPLE = color(102,0,204)
LIME = color(38,255,10)
colorList = [WHITE,RED,YELLOW,PURPLE,LIME]



class Sheep:
    def __init__(self,x,y,col):
        self.x = x
        self.y = y
        self.sz = 10 #size
        self.energy = 20
        self.col = col
        self.age = 0
        
    
    def update(self):
        move = 5
        self.energy -= 0.7
        self.sz = map(self.energy,0,50,7,15)
        if self.col== RED:
            if move < 15:
                move += 1
            if move >= 14:
                self.energy -= 0.8
        if self.col == LIME:
            move = 2
            self.energy += 0.5
            self.age -= 0.9
        if self.col == PURPLE:
            self.age += 0.5
            move = 5
        
        self.age += 1

    
            
        if self.energy <= 0:
            sheepList.remove(self)
        elif self.age > 100:
            sheepList.remove(self)
            
        if self.energy >= 50:
            if self.col == LIME:
                self.energy -= 45
            elif self.col == PURPLE:
                self.energy -= 10
                sheepList.append(Sheep(self.x+random(0,10),self.y+random(0,10),self.col))
                sheepList.append(Sheep(self.x+random(0,10),self.y+random(0,10),self.col))
                
                
                
            else:
                self.energy -= 30 #giving brith takes energy
            sheepList.append(Sheep(self.x,self.y,self.col))
            
            
        self.x += random(-move, move)
        self.y += random(-move, move)
        if self.x > width:
            self.x %= width
        if self.y > height:
            self.y %= height
        if self.x < 0:
            self.x += width
        if self.y < 0:
            self.y += height
        #find the patch of grass youre on in the grassList:
        xscl = int(self.x / patchSize)
        yscl = int(self.y / patchSize)
        grass = grassList[xscl * rows_of_grass +yscl]
        if not grass.eaten:
            self.energy += grass.energy
            grass.eaten = True
            
        fill(self.col)
        ellipse(self.x,self.y,self.sz,self.sz)
        

  
class Grass:
    def __init__(self,x,y,sz):
        self.x = x
        self.y = y
        self.energy = 4 #energy from eating
        self.eaten = False
        self.sz = sz
    
    def update(self):
        if self.eaten:
            if random(100) < 1:
                self.eaten = False
            else:
                fill(BROWN)
        else:
            fill(GREEN)
        rect(self.x,self.y,self.sz,self.sz)
    
class Wolf:
    def __init__(self,x,y,col):
        self.x = x
        self.y = y
        self.sz = 15 #size
#        self.energy = 20
        self.col = col
#        self.age = 0
    def update(self):
        move = 5
        self.x += random(-move, move)
        self.y += random(-move, move)
        if self.x > width:
            self.x %= width
        if self.y > height:
            self.y %= height
        if self.x < 0:
            self.x += width
        if self.y < 0:
            self.y += height
        fill(self.col)
        ellipse(self.x,self.y,self.sz,self.sz)         
       
        
                    
      
        
wolfList = []    
sheepList = []
grassList = []
patchSize = 5 # size of each patch of grass
                    
        
def setup():
    global rows_of_grass
    global patchSize
    size(600,600)
    rows_of_grass = height/patchSize
    noStroke()
    for a in range(1):
        wolfList.append(Wolf(random(width),
                             random(height),
                             color(200,200,200)))
    for i in range(20):
        sheepList.append(Sheep(random(width),
                               random(height),
                               choice(colorList)))
        
    for x in range(0,width,patchSize):
        for y in range(0,height,patchSize):
            grassList.append(Grass(x,y,patchSize))
    
    
def draw():
    background(WHITE)
    
    for grass in grassList:
        grass.update()
        
    for sheep in sheepList:
        sheep.update()
    for wolf in wolfList:
        wolf.update()

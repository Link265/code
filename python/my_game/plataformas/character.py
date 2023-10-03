import pygame


class Character():
    def __init__(self,window):
        self.x = 200
        self.y = 200
        self.size = 30
        self.velocity_x = 0
        self.velocity_y = 0
        self.dimensions = (self.x,self.y,self.size,self.size)
        self.window = window
        self.color = (0,0,255)#azul
    def draw(self):
        pygame.draw.rect(self.window,self.color,self.dimensions)
    def update(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.dimensions = (self.x,self.y,self.size,self.size)  
    def stop(self):
        self.velocity_x = 0
        self.velocity_y = 0
    def up(self):
        self.velocity_y = -10
    def down(self):
        self.velocity_y = 10
    def left(self):
        self.velocity_x = -10
    def right(self):
        self.velocity_x = 10        
    def controles(self,key):
        keys = {
            pygame.K_RIGHT:self.right,
            pygame.K_LEFT:self.left,
            pygame.K_DOWN:self.down,
            pygame.K_UP:self.up
        }
        keys[str(key)]()
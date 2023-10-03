import pygame
import sys
import random


pygame.init()

size =20

width = 800
height = 600


window = pygame.display.set_mode((width,height))

white = (255,255,255)
red = (255,0,0)

class Snake():
    def __init__(self):
        self.tail = [{"x":20,"y":20}]
        self.color = white
        self.size = size
        self.direction = "RIGHT"

    def draw(self):
        for i in range(len(self.tail)):    
            pygame.draw.rect(window,self.color,(self.tail[i]["x"],self.tail[i]["y"],size-2,size-2)) 

    def growth(self):
        x1 = self.tail[-1]["x"]
        y1 = self.tail[-1]["y"]
        self.tail.append({"x":x1,"y":y1})

    def eat(self):
        if self.tail[0]["x"] == apple.x and self.tail[0]["y"] == apple.y:


            self.growth()
            return True
        return False

    def move_left(self):
        if self.direction != "RIGHT":
            self.direction = "LEFT"

    def move_up(self):
        if self.direction != "DOWN":
            self.direction = "UP"
    
    def move_right(self):
        if self.direction != "LEFT":
            self.direction = "RIGHT"
    
    def move_down(self):
        if self.direction != "UP":
            self.direction = "DOWN"

    def update(self):
        

        

        if len(self.tail) > 1:
            for i in range(len(self.tail)-1,0,-1):
                
                
                self.tail[i]["x"] = self.tail[i-1]['x'] 
                
                self.tail[i]["x"] = self.tail[i-1]['x']
                
                self.tail[i]["y"] = self.tail[i-1]['y']
                
                self.tail[i]["y"] = self.tail[i-1]['y']    

        if self.direction == "RIGHT":
                self.tail[0]["x"] += self.size 
        if self.direction == "LEFT":
                self.tail[0]["x"] -= self.size
        if self.direction == "UP":
                self.tail[0]["y"] -= self.size
        if self.direction == "DOWN":
                self.tail[0]["y"] += self.size
                

class Apple():
    def __init__(self):
        self.x = random.randrange(0,width,size)
        self.y = random.randrange(0,height,size)
        self.size = size
        self.color = red
    def draw(self):
        pygame.draw.rect(window,self.color,(self.x,self.y,self.size,self.size))
    def reset(self):
        self.x = random.randrange(0,width,size)
        self.y = random.randrange(0,height,size)
snake = Snake()
apple = Apple()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.move_left()
            if event.key == pygame.K_RIGHT:
                snake.move_right()
            if event.key == pygame.K_UP:
                snake.move_up()    
            if event.key == pygame.K_DOWN:
                snake.move_down()

    #coloreando la pantalla de negro        
    window.fill((0,155,0))   

    snake.update()
    snake.draw()
    if snake.eat():
        apple.reset()
    apple.draw()

    pygame.display.flip()

    clock.tick(10)
         
import pygame
import random
import math
import time
import timeit

from pygame.constants import VIDEOEXPOSE
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0,0,255)
class Text:
    def __init__(self, screen, color, x, y):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
    def display(self, font, message):
        img = font.render(message,True, self.color)
        self.screen.blit(img, (self.x, self.y))

class Node:
    nodes = []
    def __init__(self, screen, color, x, y,gravity,initialVelocity,angle):
        self.screen = screen
        self.color = color
        self.l = 30
        self.x = x
        self.y = y
        self.dx = 0
        self.gravity = gravity
        self.initialVelocity = initialVelocity
        self.angle = angle
        self.time = 0
        self.previous_inst = "0x"
        self.flag = False
        self.vx = self.initialVelocity*math.cos(math.radians(self.angle))
        self.voy = self.initialVelocity*(math.sin(math.radians(self.angle)))
        self.h = ((self.initialVelocity**2)*math.sin(math.radians(self.angle))**2)/(2*9.81)
        

    def create(self):
        self.rect = pygame.Rect(self.x, self.y, self.l, self.l)
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self,deltaTime):
        if self.y >= 570 and self.time > 0:
            self.vy = 0
            self.vx = 0
        else:
            self.time += deltaTime
            self.x = self.vx*self.time
            self.y = ((self.voy*self.time)-(0.5*self.gravity*(self.time**2))-570)*-1
            self.nodes.append(punto(self.screen,BLUE,self.x+15,self.y+15))
class punto(Node):
    def __init__(self, screen, color, x, y):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.l = 1

def game():
    pygame.init()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("C:\Windows\Fonts\Arial", 24)
    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("Juego")
    node = Node(screen,RED,10,0,9.81,100,80)
    node2 = punto(screen,GREEN,0,0)
    start = time.time()
    timeLabel = Text(screen,GREEN,20,20)
    distanceLabel = Text(screen,GREEN,20,40)
    heightLabel = Text(screen,GREEN,20,60)
    dLabel = Text(screen,GREEN,20,80)

    run = True
    while run == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        delta = time.time() - start
        start = time.time()
        screen.fill([0,0,0])
        node.create()
        node.update(delta)
        timeLabel.display(font, f" Time: {node.time:.0f}s")
        distanceLabel.display(font, f" Height: {abs((node.y-600+30)*-1):.0f}m")
        heightLabel.display(font, f" Distance: {node.x:.0f}m")
        dLabel.display(font, f" Distance: {node.h:.0f}m")
        for i in node.nodes:
            i.create()
        pygame.display.flip()
        clock.tick()
    pygame.quit()
def main():
    game()
main()
import pygame
import sys
from pygame.locals import *



pygame.init()
vec = pygame.math.Vector2

HEIGHT = 450
WIDTH  = 400


ACC    = 0.5
FRIC   = -.1#-0.12
FPS    = 60

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("eee")

class Player(pygame.sprite.Sprite):
    
    all_images = {}
    
    def __init__(self):
        super().__init__()
      
        #self.surf = pygame.Surface((50,30)) #Is this a 30x30 square character?
        #self.surf.fill((128, 255, 40)) #Color!!!
        #self.rect = self.surf.get_rect()
        self.rect = pygame.Rect(0,0,48,48)
        #self.image = pygame.image.load("piskel.png")
        self.all_images["left"] = pygame.image.load("llama_l.png")
        self.all_images["right"] = pygame.image.load("llama_r.png")
        
        self.image = self.all_images["left"]
            
        
        self.pos=vec((10, 385))
        self.vel=vec(0,0)
        self.acc=vec(0,0)

    def update(self):
        print("collided with ground!!")
        hits = pygame.sprite.spritecollide(P1, platforms, False)
        if P1.vel.y > 0:
            if hits:
                self.pos.y = hits[0].rect.top + 1
                self.vel.y = 0
    
    def UpdateImage(self):
    
        if self.acc.x < 0:
            self.image = self.all_images["left"]
        if self.acc.x > 0:
            self.image = self.all_images["right"]
            
    def jump(self):
        self.vel.y = -15
        print("Jumping, yo!")
        print("Velocity = ", self.vel.y)
        
    def move(self):
        self.acc = vec(0,0.5)
        
        pressed_keys = pygame.key.get_pressed()
        
        #left and righ
        if pressed_keys[K_LEFT]:
            self.image = self.all_images["left"]
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.image = self.all_images["right"]
            self.acc.x = ACC
            
        #up and down
#         if pressed_keys[K_UP]:
#             self.acc.y = -ACC
#         if pressed_keys[K_DOWN]:
#             self.acc.y = ACC
            
        self.acc.x += self.vel.x * FRIC
#        self.acc.y += self.vel.y * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        
        
        
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
           
            
#         if self.pos.y > HEIGHT - 10:
#             self.pos.y = HEIGHT - 10
#             self.acc.y = 0
#         if self.pos.y < 10:
#             self.pos.y = 10
#             self.acc.y = 0
           
           
           
        #self.UpdateImage()
        self.rect.midbottom = self.pos
        
        
class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = ((WIDTH/2), (HEIGHT - 10)))
        
PT1 = platform()
P1 = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
#all_sprites.add(P1)

platforms = pygame.sprite.Group()
platforms.add(PT1)

#Game Loop

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                P1.jump()
     
    displaysurface.fill((0,0,0))
    P1.update()
 
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
    displaysurface.blit(P1.image, P1.rect)
     
 
    pygame.display.update()
    FramePerSec.tick(FPS)
    
    P1.move()
    
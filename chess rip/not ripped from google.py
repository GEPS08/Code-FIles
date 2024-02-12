import pygame
import time,os

pygame.init()

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        
        self.image = image

        self.rect = self.image.get_rect()

width = 800
height = 800

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Chess')

bg_img = pygame.image.load(r'C:\Users\Joe\.vscode\code files\chess rip\pieces\bg.png')
bg_img = pygame.transform.scale(bg_img, (width, height))

test = Sprite(r'C:\Users\Joe\.vscode\code files\chess rip\pieces\b_pawn.png')
pygame.image.load(test.image)

starting_order = {(0, 0): pygame.image.load(test.image)}

test.rect.x = 200

#b_pawn = pygame.image.load(r'C:\Users\Joe\.vscode\code files\chess rip\pieces\b_pawn.png').convert_alpha()
#b_king = pygame.image.load(r'C:\Users\Joe\.vscode\code files\chess rip\pieces\b_king.png').convert_alpha()
#b_queen = pygame.image.load(r'C:\Users\Joe\.vscode\code files\chess rip\pieces\b_queen.png').convert_alpha()
#b_knight = pygame.image.load(r'C:\Users\Joe\.vscode\code files\chess rip\pieces\b_knight.png').convert_alpha()
#b_rook = pygame.image.load(r'C:\Users\Joe\.vscode\code files\chess rip\pieces\b_rook.png').convert_alpha()
#b_bishop = pygame.image.load(r'C:\Users\Joe\.vscode\code files\chess rip\pieces\b_bishop.png').convert_alpha()

#w_pawn = pygame.image.load(r'C:\Users\Joe\.vscode\code files\chess rip\pieces\w_pawn.png').convert_alpha()
#w_king = pygame.image.load(r'C:\Users\Joe\.vscode\code files\chess rip\pieces\w_king.png').convert_alpha()
#w_queen = pygame.image.load(r'C:\Users\Joe\.vscode\code files\chess rip\pieces\w_queen.png').convert_alpha()
#w_knight = pygame.image.load(r'C:\Users\Joe\.vscode\code files\chess rip\pieces\w_knight.png').convert_alpha()
#w_rook = pygame.image.load(r'C:\Users\Joe\.vscode\code files\chess rip\pieces\w_rook.png').convert_alpha()
#w_bishop = pygame.image.load(r'C:\Users\Joe\.vscode\code files\chess rip\pieces\w_bishop.png').convert_alpha()

#b_pawn = pygame.transform.scale(b_pawn, (100, 100))
#b_king = pygame.transform.scale(b_king, (100, 100))
#b_queen = pygame.transform.scale(b_queen, (100, 100))
#b_knight = pygame.transform.scale(b_knight, (100, 100))
#b_rook = pygame.transform.scale(b_rook, (100, 100))
#b_bishop = pygame.transform.scale(b_bishop, (100, 100))

#w_pawn = pygame.transform.scale(w_pawn, (100, 100))
#w_king = pygame.transform.scale(w_king, (100, 100))
#w_queen = pygame.transform.scale(w_queen, (100, 100))
#w_knight = pygame.transform.scale(w_knight, (100, 100))
#w_rook = pygame.transform.scale(w_rook, (100, 100))
#w_bishop = pygame.transform.scale(w_bishop, (100, 100))

screen.blit(bg_img, (0, 0))

#screen.blit(b_rook, (0, 0))
#screen.blit(b_knight, (100, 0))
#screen.blit(b_bishop, (200, 0))
#screen.blit(b_queen, (400, 0))
#screen.blit(b_king, (300, 0))
#screen.blit(b_bishop, (500, 0))
#screen.blit(b_knight, (600, 0))
#screen.blit(b_rook, (700, 0))

#for x in range(8):
#  screen.blit(b_pawn, (x*100, 100))

#for x in range(8):
#  screen.blit(w_pawn, (x*100, 600))

#screen.blit(w_rook, (0, 700))
#screen.blit(w_knight, (100, 700))
#screen.blit(w_bishop, (200, 700))
#screen.blit(w_queen, (400, 700))
#screen.blit(w_king, (300, 700))
#screen.blit(w_bishop, (500, 700))
#screen.blit(w_knight, (600, 700))
#screen.blit(w_rook, (700, 700))

#def pos_pawn():

#def pos_king():

#def pos_queen():

#def pos_bishop():

#def pos_knight():

#def pos_rook():


pygame.display.flip()
status = True
while (status):
 
  # iterate over the list of Event objects
  # that was returned by pygame.event.get() method.
    for i in pygame.event.get():
 
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if i.type == pygame.QUIT:
            status = False
 
# deactivates the pygame library
pygame.quit()
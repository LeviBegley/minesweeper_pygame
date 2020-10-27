import pygame
import time
import random
import math

pygame.init()

display_width = 1000
display_height = 1000

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

grid_width = 1000
grid_hight = 1000

board = {
    }
bombs = []

listoflists = []

num = 0
while num != 8:
    random_list = []
    for i in range(8):
        d = random.randint(0,6)
        if d == 1:
            random_list.append("B")
            p = [num, i]
            bombs.append(p)

#             try:
#                 if random_list[num -  2] in (0, 1, 2, 3, 4):
#                     random_list[num -  2] += 0
#                 yepclock = 1
#             except:
#                 yepclock = 0
#             if yepclock == 1:
#                 if random_list[num -  2] in (0, 1, 2, 3, 4):
#                       random_list[num -  2] += 1
        else:
            random_list.append(0)
        #random_list.append(n)
    #print(random_list)
    listoflists.append((list(random_list)))
    num += 1
print(listoflists)

for i in bombs:
    left = [i[0], (i[1] - 1)]
    right = [i[0], (i[1] + 1)]
    up = [(i[0] - 1), i[1]]
    down = [(i[0] + 1), i[1]]
    up_left = [(i[0] - 1), (i[1] - 1)]
    up_right = [(i[0] - 1), (i[1] + 1)]
    down_left = [(i[0] + 1), (i[1] - 1)]
    down_right = [(i[0] + 1), (i[1] + 1)]

    sur_hight = left[0] 
    sur_width = left[1]
    if sur_width > -1:
        try:
            (listoflists[sur_hight][sur_width]) = (listoflists[sur_hight][sur_width]) + 1
        except:
            pass
        
    sur_hight = right[0] 
    sur_width = right[1]
    if sur_width < 9:
        try:
            (listoflists[sur_hight][sur_width]) = (listoflists[sur_hight][sur_width]) + 1
        except:
            pass
        
    sur_hight = up[0] 
    sur_width = up[1]
    if sur_hight > -1:
        try:
            (listoflists[sur_hight][sur_width]) = (listoflists[sur_hight][sur_width]) + 1
        except:
            pass
        
    sur_hight = down[0] 
    sur_width = down[1]
    if sur_hight < 9:
        try:
            (listoflists[sur_hight][sur_width]) = (listoflists[sur_hight][sur_width]) + 1
        except:
            pass
        
    sur_hight = up_left[0] 
    sur_width = up_left[1]
    if sur_width > -1:
        if sur_hight > -1:
            try:
                (listoflists[sur_hight][sur_width]) = (listoflists[sur_hight][sur_width]) + 1
            except:
                pass
            
    sur_hight = up_right[0] 
    sur_width = up_right[1]
    if sur_width < 9:
        if sur_hight > -1:
            try:
                (listoflists[sur_hight][sur_width]) = (listoflists[sur_hight][sur_width]) + 1
            except:
                pass
            
    sur_hight = down_left[0] 
    sur_width = down_left[1]
    if sur_width > -1:
        if sur_hight > -1:
            try:
                (listoflists[sur_hight][sur_width]) = (listoflists[sur_hight][sur_width]) + 1
            except:
                pass
            
    sur_hight = down_right[0] 
    sur_width = down_right[1]
    if sur_width < 9:
        if sur_hight < 9:
            try:
                (listoflists[sur_hight][sur_width]) = (listoflists[sur_hight][sur_width]) + 1
            except:
                pass
            
        
        
print(listoflists[0])
print(listoflists[1])
print(listoflists[2])
print(listoflists[3])
print(listoflists[4])
print(listoflists[5])
print(listoflists[6])
print(listoflists[7])

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Bailz54')
clock = pygame.time.Clock()

grid = pygame.image.load('grid.png')

def car(x,y):
    gameDisplay.blit(grid,(x,y))



x =  (display_width * 0.45)
y = (display_height * 0.8)
    

def crash():
    message_display('oh no')
    
def game_loop():
    x = (display_width * 0)
    y = (display_height * 0)

    x_change = 0
    y_change = 0
    
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        gameDisplay.fill(white)
        car(x,y)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            #print(pos)
            grod = (pos[0] / 125)
            crub = (pos[1] / 125)
            grod = int(grod) + 1
            crub = int(crub) + 1
            print(grod)
            print(crub)
            list1 = listoflists[crub - 1]
            list2 = list1[grod - 1]
            if list2 == "B":
                pygame.quit()
                quit()
                
                
                
                

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()

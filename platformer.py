import pygame
pygame.init()  
pygame.display.set_caption("easy platformer")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop


k2 = pygame.mixer.Sound("2WUUMYH-pirate-jumping-jump.mp3")



#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3
W=0
A = 1
D = 2



#player variables
xpos = 500 #xpos of player
ypos = 200 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player

xpos2 = 100 #xpos of player
ypos2 = 200 #ypos of player
vx2 = 0 #x velocity of player
vy2 = 0 #y velocity of player
keys = [False, False, False, False] #this list holds whether each key has been pressed
keys2 = [False, False, False, False]
isOnGround = False #this variable stops gravity from pulling you down more when on a platform
isOnGround2 = False


while not gameover: #GAME LOOP############################################################
    clock.tick(60) #FPS
   
    #Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
     
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=True
            elif event.key == pygame.K_UP:
                keys[UP]=True
            elif event.key == pygame.K_a:
                keys2[LEFT]=True
            elif event.key == pygame.K_d:
                keys2[RIGHT]=True
            elif event.key == pygame.K_w:
                keys2[UP]=True
       
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False
            elif event.key == pygame.K_UP:
                keys[UP]=False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=False  
            elif event.key == pygame.K_a:
                keys2[LEFT]=False
            elif event.key == pygame.K_d:
                keys2[RIGHT]=False
            elif event.key == pygame.K_w:
                keys2[UP]=False
         
         
    #physics section--------------------------------------------------------------------
    #LEFT MOVEMENT
    if keys[LEFT]==True:
        vx=-3
       
   
    elif keys[RIGHT]==True:
        vx=+3
       
   

    #turn off velocity
    else:
        vx = 0
        #JUMPING
    if keys[UP] == True and isOnGround == True: #only jump when on the ground
        vy = -8
        isOnGround = False
        direction = UP
        pygame.mixer.Sound.play(k2)
       
   #PLAYER 2=================================
    if keys2[LEFT]==True:
        vx2=-3
       
   
    elif keys2[RIGHT]==True:
        vx2=+3
       
   

    #turn off velocity
    else:
        vx2 = 0
        #JUMPING
    if keys2[UP] == True and isOnGround == True: #only jump when on the ground
        vy2 = -8
        isOnGround = False
        direction = UP
        pygame.mixer.Sound.play(k2)
   

   
    #COLLISION
    if xpos>100 and xpos<200 and ypos+40 >750 and ypos+40 <770:
        ypos = 750-40
        isOnGround = True
        vy = 0
    elif xpos>200 and xpos<300 and ypos+40 >650 and ypos+40 <670:
        ypos = 650-40
        isOnGround = True
        vy = 0
    elif xpos>300 and xpos<400 and ypos+40 >550 and ypos+40 <570:
        ypos = 550-40
        isOnGround = True
        vy = 0
    elif xpos>400 and xpos<500 and ypos+40 >450 and ypos+40 <470:
        ypos = 450-40
        isOnGround = True
        vy = 0
    elif xpos>500 and xpos<600 and ypos+40 >350 and ypos+40 <370:
        ypos = 350-40
        isOnGround = True
        vy = 0
    elif xpos>300 and xpos<400 and ypos+40 >250 and ypos+40 <270:
        ypos = 250-40
        isOnGround = True
        vy = 0
    elif xpos>200 and xpos<300 and ypos+40 >150 and ypos+40 <170:
        ypos = 150-40
        isOnGround = True
        vy = 0
       
    else:
        isOnGround = False


   
    #stop falling if on bottom of game screen
    if ypos > 760:
        isOnGround = True
        vy = 0
        ypos = 760
   
    #gravity
    if isOnGround == False:
        vy+=.2 #notice this grows over time, aka ACCELERATION
       
    #stop falling if on bottom of game screen
    if ypos2 > 760:
        isOnGround2 = True
        vy2 = 0
        ypos2 = 760
   
    #gravity
    if isOnGround2 == False:
        vy2+=.2 #notice this grows over time, aka ACCELERATION
   

    #update player position
    xpos+=vx
    ypos+=vy
   
    xpos2+=vx2
    ypos2+=vy2
   
 
    # RENDER Section--------------------------------------------------------------------------------
           
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
 
    pygame.draw.rect(screen, (255, 204, 229), (xpos, ypos, 20, 40))
    pygame.draw.rect(screen, (204, 0, 102), (xpos2, ypos2, 30, 50))
    #first platform
    pygame.draw.rect(screen, (200, 0, 100), (100, 750, 100, 20))
   
    #second platform
    pygame.draw.rect(screen, (100, 0, 200), (200, 650, 100, 20))
   
    pygame.draw.rect(screen, (0, 255, 0), (300, 550, 100, 20))
   
    pygame.draw.rect(screen, (0, 255, 0), (400, 450, 100, 20))
   
    pygame.draw.rect(screen, (0, 255, 0), (500, 350, 100, 20))
   
    pygame.draw.rect(screen, (0, 255, 0), (300, 250, 100, 20))
   
    pygame.draw.rect(screen, (0, 255, 0), (200, 150, 100, 20))
   
   
    pygame.display.flip()#this actually puts the pixel on the screen
   
#end game loop------------------------------------------------------------------------------
pygame.quit()


import pygame,time,random

pygame.init()
SnakeWidth=10
SnakeHeight=10
GameHeight=500
GameWidth=600
FoodWidth=10
FoodHeight=10
x=random.randrange(0,(GameWidth-9),10)
y=random.randrange(0,(GameHeight-9),10)
Foodx=random.randrange(0,(GameWidth-9),10)
Foody=random.randrange(0,(GameHeight-9),10)
xMove = 0
yMove = 0
b=True
v=True
Tallx=10
Tally=0
left=False
right=False
up=False
down=False
pause=False
SnakeArr=[]
SnakePlace=[0]
   
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
yellow = (255,255,0)

   
gameDisplay = pygame.display.set_mode((GameWidth,GameHeight))
pygame.display.set_caption("Snake By Okasha")

font=pygame.font.SysFont("comicsansms",90,True)
SpaceFont=pygame.font.SysFont("comicsansms",40,True)

NotExit=True
while NotExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            NotExit=False
            
        if event.type == pygame.KEYDOWN:    
            if (event.key == pygame.K_SPACE):
                pause =True
                gameDisplay.blit(font.render("PAUSE",True , yellow),(135,GameHeight/3))
                pygame.display.update()
                while pause == True:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:    
                            if (event.key == pygame.K_SPACE):
                                pause=False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if right == True :
                    pass
                else:
                    xMove = -10
                    yMove = 0
                    left=True
                    right=False
                    up=False
                    down=False
            elif event.key == pygame.K_RIGHT:
                if left == True :
                    pass
                else:
                    xMove = 10
                    yMove = 0
                    left=False
                    right=True
                    up=False
                    down=False
            if event.key == pygame.K_UP:
                if down == True :
                    pass
                else:
                    yMove = -10
                    xMove = 0
                    left=False
                    right=False
                    up=True
                    down=False
            elif event.key == pygame.K_DOWN:
                if up == True :
                    pass
                else:
                    yMove = 10
                    xMove = 0
                    left=False
                    right=False
                    up=False
                    down=True
            
    x1=x
    y1=y
    x += xMove
    y += yMove
    
    gameDisplay.fill(black)
    
    food=pygame.Rect(Foodx,Foody,FoodWidth,FoodHeight)
    pygame.draw.rect(gameDisplay,red,food)
    
    snake= pygame.Rect(x,y,SnakeWidth,SnakeHeight)
    pygame.draw.rect(gameDisplay,white,snake)
    
    
    
    if x == Foodx and y == Foody:
        Foodx=(random.randrange(0,(GameWidth-9),10))
        Foody=(random.randrange(0,(GameHeight-9),10))
        xn=x
        yn=y
        w=len(SnakeArr)
        if left==True:
            xn = x+((w+1)*10)
        elif right==True:
            xn= x-((w+1)*10) 
        elif up==True:
            yn= y+((w+1)*10)
        elif down==True:
            yn = y-((w+1)*10)
        snake= pygame.Rect(xn,yn,SnakeWidth,SnakeHeight)
        SnakeArr.append(snake)
        SnakePlace.append((xn,yn))

    SnakePlace[0]=(x1,y1)

    a= False
    q=1
    i=len(SnakePlace)-1
    
    for Snakes in SnakeArr:
        SnakePlace[i]=SnakePlace[i-1]
        (xn,yn)=SnakePlace[i]
        
        pygame.draw.rect(gameDisplay,white,(xn,yn,SnakeWidth,SnakeHeight))
        i-=1
        if (x,y) == SnakePlace[q]:
            a=True
            break
        q+=1
        
    while(a):
            pygame.display.update()
            gameDisplay.fill(black)
            gameDisplay.blit(font.render("YOU LOST! ",True , yellow),(30,GameHeight/5))
            gameDisplay.blit(SpaceFont.render("Press Space to play again",True , yellow),(80,GameHeight/2))  
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_SPACE):
                        yMove=xMove=0
                        SnakeArr=[]
                        SnakePlace=[0]
                        x=random.randrange(0,(GameWidth-9),10)
                        y=random.randrange(0,(GameHeight-9),10)
                        Foodx=random.randrange(0,(GameWidth-9),10)
                        Foody=random.randrange(0,(GameHeight-9),10)
                        a=False
                elif event.type == pygame.QUIT:
                    quit()
        
    for axis in (SnakePlace):
        if (Foodx,Foody) == axis:
            v=True
        else :
            v=False
        while v:
            Foodx=random.randrange(0,(GameWidth-9),10)
            Foody=random.randrange(0,(GameHeight-9),10)
            if (foodx,foody) != axis:
                 v=False

             
    if x<0 or y<0 or x>GameWidth-10 or y>GameHeight-10:
        yMove=xMove=0
        SnakeArr=[]
        SnakePlace=[0]
        b=True
        while(b):
            pygame.display.update()
            gameDisplay.fill(black)
            gameDisplay.blit(font.render("YOU LOST! ",True , yellow),(30,GameHeight/5))
            gameDisplay.blit(SpaceFont.render("Press Space to play again",True , yellow),(80,GameHeight/2))
            x=random.randrange(0,(GameWidth-9),10)
            y=random.randrange(0,(GameHeight-9),10)
            Foodx=random.randrange(0,(GameWidth-9),10)
            Foody=random.randrange(0,(GameHeight-9),10)
            b = True
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_SPACE):
                        b=False
                elif event.type == pygame.QUIT:
                    quit()


    if len(SnakePlace) == 3000:
        gameDisplay.blit(font.render("YOU Won! ",True , yellow),(30,GameHeight/5))
        time.sleep(.06)
        quit()

    pygame.display.update()
    time.sleep(.06)
            
pygame.quit()
quit()

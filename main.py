#Carlos Rodriguez
#modules
import pygame
import random
import time
from pygame import mixer

pygame.init()
pygame.mixer.init()

# the display size
displayX = 800
displayY = 700
displayC=(600,500)
#setting the display and caption for the game
ses = pygame.display.set_mode((displayX , displayY))
pygame.display.set_caption('Snake game by Carlos')
# colors 
white = (255, 255, 255)
purple = (186, 3, 252)
red = (168, 20, 60)
blue = (32, 45, 227)
yellow = (168, 136, 49)
green = (186,255,201)
gray = (128, 128, 128)

# variables
block = 10
clock = pygame.time.Clock()

#fonts
font = pygame.font.SysFont(None, 50)
font1=pygame.font.SysFont("impact",20)

# game over message function
def displayingMes (msg, color):
    message=font1.render(msg, True, color)
    ses.blit(message, [displayX/10, displayY/4])

#snake display
def mySnake(block, snakeList):
    for x in snakeList:
        pygame.draw.rect(ses, blue, [x[0], x[1], block, block])

#displaying score
def Myscore(score):
    value = font1.render("your score:"+str(score),True,yellow)
    ses.blit(value,[0,0])

#background picture display
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
#unfinished food class
class Food:
    block_size = None
    color = (168, 20, 60)
    x = 0;
    y = 0;
    bounds = None

    def __init__(self, block_size, bounds):
        self.block_size = block_size
        self.bounds = bounds

    def draw(self, game, ses):
        game.draw.rect(ses, self.color, (self.x, self.y, self.block_size, self.block_size))

    def respawn(self):
        blocks_in_x = (self.bounds[0])/self.block_size;
        blocks_in_y = (self.bounds[1])/self.block_size;
        self.x = random.randint(0, blocks_in_x - 1) * self.block_size
        self.y = random.randint(0, blocks_in_y - 1) * self.block_size

    def eat(self):
        self.lengthSnake += 1

    # sees if the head of the snake is over the food
    def check_for_food(self, food):
        head = self.body[-1]
        if head[0] == food.x and head[1] == food.y:
            self.eat()
            food.respawn()


#UNFINISHED game class
class GameState():
    def __init__(self):
        self.state='mainGame'
    def level3(self):
        gameOver = False
        closeGame = False
        x1 = displayX / 2
        y1 = displayY / 2
        x1Change = 0
        y1Change = 0
        clock = pygame.time.Clock()
        speed = 30
        snakeList = []
        lengthSnake = 1


        # setting the foods random location
        foodX = round(random.randrange(0, displayX - block) / 10.0) * 10.0
        foodY = round(random.randrange(0, displayY - block) / 10.0) * 10.0

        while not gameOver:
            # Displayed message after losing
            while closeGame == True:
                BackGround = Background('level3.jpg', [0, 0])
                ses.fill(gray)
                ses.blit(BackGround.image, BackGround.rect)

                displayingMes("Level 3 Game Over! press q to quit or press r to restart", red)
                Myscore(lengthSnake - 1)
                pygame.display.update()

                # to loop the game using r and q
                for r in pygame.event.get():
                    if r.type == pygame.KEYDOWN:
                        if r.key == pygame.K_q:
                            gameover = True
                            closeGame = False
                        if r.key == pygame.K_r:
                            self.level3()

            # snake controls
            for r in pygame.event.get():
                if r.type == pygame.QUIT:
                    gameOver = True
                if r.type == pygame.KEYDOWN:
                    if r.key == pygame.K_LEFT:
                        x1Change = -block
                        y1Change = 0
                    elif r.key == pygame.K_RIGHT:
                        x1Change = block
                        y1Change = 0
                    elif r.key == pygame.K_UP:
                        x1Change = 0
                        y1Change = -block
                    elif r.key == pygame.K_DOWN:
                        x1Change = 0
                        y1Change = block

            # bounadries for the snake
            if x1 >= displayX or x1 < 0 or y1 >= displayY or y1 < 0:
                closeGame = True
            x1 += x1Change
            y1 += y1Change

            # graphic background
            BackGround = Background('level3.jpg', [0, 0])
            ses.fill(gray)
            ses.blit(BackGround.image, BackGround.rect)

            # to get the food on the screen
            pygame.draw.rect(ses, red, [foodX, foodY, block, block])

            # increasing snake body
            head = []
            head.append(x1)
            head.append(y1)
            snakeList.append(head)
            if len(snakeList) > lengthSnake:
                del snakeList[0]
            for y in snakeList[:-1]:
                if y == head:
                    closeGame = True
            mySnake(block, snakeList)
            Myscore(lengthSnake)
            pygame.display.update()
            clock.tick(speed)

            #  when snake collides  with food
            if x1 == foodX and y1 == foodY:

                foodX = round(random.randrange(1, displayX - block) / 10.0) * 10.0
                foodY = round(random.randrange(1, displayX - block) / 10.0) * 10.0
                lengthSnake += 1


    #second level code
    def level2 (self):

        #main game variables
        gameOver = False
        closeGame = False
        x1 = displayX / 2
        y1 = displayY / 2
        x1Change = 0
        y1Change = 0
        clock = pygame.time.Clock()
        speed = 20
        snakeList = [ ]
        lengthSnake = 1

        #setting the foods random location
        foodX = round(random.randrange(0, displayX - block) / 10.0) * 10.0
        foodY = round(random.randrange(0, displayY - block) / 10.0) * 10.0

        while not gameOver:
            # Displayed message after losing
            while closeGame == True:
                BackGround = Background('please.jpg', [0, 0])
                ses.fill(gray)
                ses.blit(BackGround.image, BackGround.rect)

                displayingMes("Level 2 Game Over! press q to quit or press r to restart", red)
                Myscore(lengthSnake - 1)
                pygame.display.update()

               #to loop the game using r and q
                for r in pygame.event.get():
                    if r.type == pygame.KEYDOWN:
                        if r.key == pygame.K_q:
                            gameover = True
                            closeGame = False
                        if r.key == pygame.K_r:
                            self.level2()

            # snake controlssss
            for r in pygame.event.get():
                if r.type == pygame.QUIT:
                    gameOver = True
                if r.type == pygame.KEYDOWN:
                    if r.key == pygame.K_LEFT:
                        x1Change = -block
                        y1Change = 0
                    elif r.key == pygame.K_RIGHT:
                        x1Change = block
                        y1Change = 0
                    elif r.key == pygame.K_UP:
                        x1Change = 0
                        y1Change = -block
                    elif r.key == pygame.K_DOWN:
                        x1Change = 0
                        y1Change = block

            # bounadries for the snake
            if x1 >= displayX or x1 < 0 or y1 >= displayY or y1 < 0:
                closeGame = True
            x1 += x1Change
            y1 += y1Change

            # graphic background
            BackGround = Background('please.jpg', [0, 0])
            ses.fill(gray)
            ses.blit(BackGround.image, BackGround.rect)

            # to get the food on the screen
            pygame.draw.rect(ses, red, [foodX, foodY, block, block])

            # increasing snake body
            head = []
            head.append(x1)
            head.append(y1)
            snakeList.append(head)
            if len(snakeList) > lengthSnake:
                del snakeList[0]
            for y in snakeList[:-1]:
                if y == head:
                    closeGame = True
            mySnake(block, snakeList)
            Myscore(lengthSnake)
            pygame.display.update()
            clock.tick(speed)



            #  when snake collides  with food
            if x1 == foodX and y1 == foodY:


                foodX = round(random.randrange(1, displayX - block) / 10.0) * 10.0
                foodY = round(random.randrange(1, displayX - block) / 10.0) * 10.0
                lengthSnake += 1
            if lengthSnake == 10:

                self.level3()

    #main game code
    def mainGame(self):

        #main game variables
        gameOver = False
        closeGame = False
        x1 = displayX / 2
        y1 = displayY / 2
        x1Change = 0
        y1Change = 0
        clock = pygame.time.Clock()
        speed = 10
        snakeList = [ ]
        lengthSnake = 1

        #setting the foods random location
        foodX = round(random.randrange(0, displayX - block) / 10.0) * 10.0
        foodY = round(random.randrange(0, displayY - block) / 10.0) * 10.0

        while not gameOver:
            # Displayed message after losing
            while closeGame == True:
                BackGround = Background('trenchGrass.jpg', [0, 0])
                ses.fill(gray)
                ses.blit(BackGround.image, BackGround.rect)

                displayingMes("Level 1 Game Over! press q to quit or press r to restart", red)
                Myscore(lengthSnake - 1)
                pygame.display.update()

               #to loop the game using r and q
                for r in pygame.event.get():
                    if r.type == pygame.KEYDOWN:
                        if r.key == pygame.K_q:
                            gameover = True
                            closeGame = False
                        if r.key == pygame.K_r:
                            self.mainGame()

            # snake controls
            for r in pygame.event.get():
                if r.type == pygame.QUIT:
                    gameOver = True
                if r.type == pygame.KEYDOWN:
                    if r.key == pygame.K_LEFT:
                        x1Change = -block
                        y1Change = 0
                    elif r.key == pygame.K_RIGHT:
                        x1Change = block
                        y1Change = 0
                    elif r.key == pygame.K_UP:
                        x1Change = 0
                        y1Change = -block
                    elif r.key == pygame.K_DOWN:
                        x1Change = 0
                        y1Change = block

            # bounadries for the snake
            if x1 >= displayX or x1 < 0 or y1 >= displayY or y1 < 0:
                closeGame = True
            x1 += x1Change
            y1 += y1Change

            # graphic background
            BackGround = Background('trenchGrass.jpg', [0, 0])
            ses.fill(gray)
            ses.blit(BackGround.image, BackGround.rect)

            # to get the food on the screen
            pygame.draw.rect(ses, red, [foodX, foodY, block, block])

            # increasing snake body
            head = []
            head.append(x1)
            head.append(y1)
            snakeList.append(head)
            if len(snakeList) > lengthSnake:
                del snakeList[0]
            for y in snakeList[:-1]:
                if y == head:
                    closeGame = True
            mySnake(block, snakeList)
            Myscore(lengthSnake)
            pygame.display.update()
            clock.tick(speed)



            #  when snake collides  with food
            if x1 == foodX and y1 == foodY:
                '''crunch = ('AppleCrunch.ogg')
                mixer.init()
                mixer.music.load(crunch)
                mixer.music.play()'''
                # mixer.music.pause()
                foodX = round(random.randrange(1, displayX - block) / 10.0) * 10.0
                foodY = round(random.randrange(1, displayX - block) / 10.0) * 10.0
                lengthSnake += 1


            if lengthSnake == 4:

                self.level2()
gameState=GameState()
#To lopp the game
while True:
    gameState.level2()


# displaying you lost message
    pygame.quit()
    quit()


                #getting to level 2
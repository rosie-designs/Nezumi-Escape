########################################################################################################
#File Name: main
#Desc: Mario but a cat
#Date: April 25, 2022
########################################################################################################
#MAKE THE INDEX DEPENDENT ON THE RAT0, RAT1, RAT2, OF THE LIST

import pygame
pygame.init()
WIDTH = 800
HEIGHT = 600
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))
keys = pygame.key.get_pressed()

#CONSTANTS
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0,0,0)
NAVY = (55, 44, 83)
GRAVITY = 2

#MOUSE MOVEMENT
mouseX = 0
mouseY = 0

#SCREEN SETTINGS (true and falses for different screens)
openingScreen = True
settingScreen = False   
gameStoryStart = False
gameBeachExploration = False
exitScreen = False
levelsScreen = False
levelSelect = False
gameEndScreen = False

#SETTINGS SCREEN PROPERTIES
nameFont = pygame.font.SysFont('Calibri', 30)
userName = ''
settingScreenPicture = pygame.image.load("settingScreen.png")
musicControl = pygame.image.load("musicButton.png")
music = True #used to mute the music
musicControlX = 440 #setting button coordinates
musicControlY = 210
backButtonX = 344 
backButtonY = 434

#TYPEWRITER FONT
typeFont = pygame.font.SysFont('Times New Roman', 30) #TYPEWRITER
typing = True

#LEVEL COMPLETIONS
beachLevelCompletion = False
forestLevelCompletion = False

#LEVEL VARIABLES
levelChosen = "beach"
levelReset = True

lastMove = "none"
catReset = "none"
air = True

#CAT VARIABLES
catX = 0
catY = 330
catW = 72
catH = 99
catMX = 10
catMY = 0
catJump = -30

#CAT ANIMATION PROPERTIES
catPicIndex = 0
catPicList_R = [0]*10
catPicList_L = [0]*10
jumpDir = ''
catWalk0Pic = pygame.image.load("catWalk0.png")
catPicList_UP = [pygame.image.load("catJumpR_stand.png"), pygame.image.load("catJumpR.png"), pygame.image.load("catJumpL_stand.png"), pygame.image.load("catJumpL.png")]
for i in range(10):
    catPicList_R[i] = pygame.image.load("catWalk" + str(i) + ".png") # setting each element to a picture
    catPicList_L[i] = pygame.image.load("LcatWalk" + str(i) + ".png")

#RAT SPRITE IMAGES
for i in range(10):
    catPicList_R[i] = pygame.image.load("catWalk" + str(i) + ".png") # setting each element to a picture
    catPicList_L[i] = pygame.image.load("LcatWalk" + str(i) + ".png")

#RAT PROPERTIES
ratW = 30
ratH = 20
ratPicList = [0]*6
for i in range(6):
    ratPicList[i] = pygame.image.load("rat" + str(i) + ".png")
ratPicListR = [ratPicList[:3]]
ratPicListL = [ratPicList[3:]]
ratIndexList = []

#GRENADE PROPERTIES
grenadeActivation = False
grenadeImg = pygame.image.load('pickupGrenade.png')
grenadeNum = 0
grenadePickup = pygame.image.load('pickupGrenade.png')
explosionAnimationList = [0]*34
for i in range(34):
    explosionAnimationList[i] = pygame.image.load("img_" + str(i) + ".png")
grenades2 = pygame.image.load('grenades2.png')
grenades3 = pygame.image.load('grenades3.png')

#SOUNDS
catMEow = pygame.mixer.Sound("catOw.ogg")
catMEow.set_volume(0.5)

#BEACH LEVEL SPRITES AND VARIABLES (Rosie)

lvl_1_Background = pygame.image.load('1LEVEL.png')
lvl_1_BackgroundFlip = pygame.image.load('1LEVELFLIP.png')
terrain3x2 = pygame.image.load('terrain(240x160).png') #check this file
terrain4x2 = pygame.image.load('terrain(320x160).png')
terrain5x2 = pygame.image.load('terrain(400x160).png')
crate1x1 = pygame.image.load('crate(1x1).png')
crate2x1 = pygame.image.load('crate(2x1).png')
crate3x1 = pygame.image.load('crate(3x1).png')
crate4x1 = pygame.image.load('crate(4x1).png')

#Decor Sprites
bigTree1 = pygame.image.load('bigTree1.png')
bigTree2 = pygame.image.load('bigTree2.png')
smallTree = pygame.image.load('smallTree.png')
woodSign = pygame.image.load('woodSign.png')
rockArrows = pygame.image.load('rockArrows.png')
sandCastle = pygame.image.load('sandCastle.png')
coral = pygame.image.load('coral.png')
mushroomShort = pygame.image.load('mushroomShort.png')
mushroomMed = pygame.image.load('mushroomMed.png')
mushroomTall = pygame.image.load('mushroomTall.png')

#Deadly Obstacles Sprites
spikes2 = pygame.image.load('deathSpikes2.png')
spikes3 = pygame.image.load('deathSpikes3.png')

#FOREST LEVEL SPRITES AND VARIABLES (Katelyn)

forestBackground1 = pygame.image.load("forestBackground1.png")
forestBackground2 = pygame.image.load("forestBackground2.png")
forestBlock3x1 = pygame.image.load("forestBlock3x1.png")
forestBlock3x1x3 = pygame.image.load("forestBlock3x1x3.png")
forestBlock3x2x2 = pygame.image.load("forestBlock3x2x2.png")
forestBlock3x2 = pygame.image.load("forestBlock3x2.png")
woodBlock1 = pygame.image.load("woodBlock1.png")
woodBlock2x1 = pygame.image.load("woodBlock2x1.png")
woodBlock3x1 = pygame.image.load("woodBlock3x1.png")
woodBlock4x1 = pygame.image.load("woodBlock4x1.png")
woodBlock5x1 = pygame.image.load("woodBlock5x1.png")
forestWater = pygame.image.load("forestWater.png")

sign1 = pygame.image.load("sign1.png")
sign2 = pygame.image.load("sign2.png")
flower1 = pygame.image.load("flower1.png")
flower2 = pygame.image.load("flower2.png")
fence1 = pygame.image.load("fence1.png")

#FUNCTIONS =========================================================================================================================================================================================

def typewriter(message, messageX, messageY): #(Rosie) Displays message in a typewriting effect
    content = ''
    for character in message: #loops through the entire message
        content += character #concatenates each letter to this variable
        gameWindow.blit(typeFont.render(content, 1, NAVY), (messageX, messageY)) 
        pygame.display.update()
        pygame.time.wait(100) #delays to make a typewriting effect

def scrollingBackground(levelBackground1, levelBackground2): #(Rosie)
    gameWindow.blit(levelBackground1, (levelBackground1X, levelBackground1Y))
    gameWindow.blit(levelBackground2, (levelBackground2X, levelBackground2Y))

def rectCollide(catRect, rectList): #(Katelyn) Checks if cat collides with rectangles in a list and returns true or false
    if catRect.collidelist(rectList)!= -1:
        return True
    elif catRect.collidelist(rectList)== -1:
        return False

def rectCollideIndexFinder(catRect, rectList): #(Katelyn) Checks if cat collides with rectangles in a list and returns index 
    for i in rectList:
        if catRect.colliderect(i):
            return (i)

def drawSprites(spriteList): #(Katelyn) draws sprites in list
    for i in range(len(spriteList)):
        gameWindow.blit(spriteList[i][2],(spriteList[i][0], spriteList[i][1]))

def itemShift(listOfItems, shift): #(Katelyn) Shifts items with scrolling background
    for i in range(len(listOfItems)):
        listOfItems[i][0] += shift
    return listOfItems

def catAnimation(direction): #Rosie
    if direction == "right":
        nextCatPic = catPicList_R[catPicIndex//2]
    elif direction == "left":
        nextCatPic = catPicList_L[catPicIndex//2]
    elif direction == "up":
        nextCatPic = catPicList_UP[catPicIndex]
    else:
        nextCatPic = catWalk0Pic
    return nextCatPic

def grenadeCounter(grenadeNum):
    if grenadeNum == 3:
        gameWindow.blit(grenades3, (30, 30))
        instructions = nameFont.render('Press Space To Shoot Grenades', 1, NAVY)
        
        gameWindow.blit(instructions, (400, 30))
    elif grenadeNum == 2:
        gameWindow.blit(grenades2, (30, 30))
    elif grenadeNum == 1:
        gameWindow.blit(grenadePickup, (30, 30))


#RAT FUNCTION: Rosie
class ratEnemy(pygame.sprite.Sprite):
    def __init__(self, ratX, ratY, speed, direction, ratNum): #setting parameters
        pygame.sprite.Sprite.__init__(self)
        self.ratPicIndex = 0 #setting each parameter to its unique variable so it can be used inside the class
        self.speed = speed
        self.ratPicIndex = 0
        self.x = ratX
        self.y = ratY
        self.direction = direction
        self.ind = ratNum
    def movement(self, ratLimitL, ratLimitR, scrollingDir): #setting variables here, so it updates each loop
        self.ratNum = ratIndexList.index(self.ind) #the index number has to be updated since the items from the list are being deleted (eg. when the cat kills the rat with the grenade)
        self.ratLimitL = ratLimitL[self.ratNum][0] 
        self.ratLimitR = ratLimitR[self.ratNum][0]
        self.scrollingDir = scrollingDir
        ratMX = 0 #controls the speed/shift of the rat
        if self.direction == 'right':
            ratMX = self.speed
        elif self.direction == 'left':
            ratMX = -self.speed #in order to move left, ratMX must be negative
        #preventing the rat from randomly stopping and speeding up
        if self.direction == 'right' and self.scrollingDir == 'left': #when the cat is chasing the rat and they're facing the same direction, it used to speed up, now it stays the same speed
            ratMX = 0
        elif self.direction == 'left' and self.scrollingDir == 'left': #when the cat and the rat are facing each other, the rat would appear to stop, but it was just scrolling with the background. Thus, now to prevent that, the speed is doubled.
            ratMX = (-self.speed)*2
        elif self.direction == 'right' and self.scrollingDir == 'right':
            ratMX = (self.speed)*2
        elif self.direction == 'left' and self.scrollingDir == 'right':
            ratMX = 0
        self.x += ratMX
        if self.direction == 'right' and self.x >= self.ratLimitR - 30: #self.x is the top left corner, so we must subtract the rat's width from the right limit
            self.direction = 'left'
            self.ratPicIndex = 0 #resetting the animation
        if self.direction == 'left' and self.x <= self.ratLimitL:
            self.direction = 'right'
            self.ratPicIndex = 0
    def draw(self):
        self.ratAnimation() #does the ratAnimation function first
        gameWindow.blit(self.ratPic, (self.x, self.y))
        del ratEnemyRectList[self.ratNum] #updating the rectangle list with new x,y coordinates
        ratEnemyRectList.insert(self.ratNum, [self.x, self.y, self.ratW, self.ratH])
        #pygame.draw.rect(gameWindow, WHITE, (ratEnemyRectList[self.ratNum]), 1) #drawing a rectangle around the rat (will delete after)
        self.ratPicIndex += 1 #cycles through the next picture for the rat animation
    def ratAnimation(self):
        if self.ratPicIndex > 8: #there is a total of 3 pictures (0 to 2) for the rat animation, but to extend the time each picture shows, we multiply the total by 4
            self.ratPicIndex = 0
        if self.direction == 'right':
            self.ratPic = ratPicListR[0][int(self.ratPicIndex//4)] #depending on the direction, a unique list of pictures is accessed
        elif self.direction == 'left':
            self.ratPic = ratPicListL[0][int(self.ratPicIndex//4)] #must floor divide by 4 b/c the indexes of the list range from 0 to 2
        self.rect = self.ratPic.get_rect()
        self.ratW = self.rect.width
        self.ratH = self.rect.height

class grenadePowerup(pygame.sprite.Sprite):
    def __init__(self, grenadeX, grenadeY, grenadeSpeed, grenadeDirection, powerupPic):
        pygame.sprite.Sprite.__init__(self)
        self.x = grenadeX
        self.y = grenadeY
        self.vel_y = -40
        self.speed = grenadeSpeed
        self.direction = grenadeDirection
        self.pic = powerupPic
        self.rect = self.pic.get_rect()
        self.w = self.rect.width
        self.h = self.rect.height
        self.explosionAnim = False
        self.removed = True #set this to true, b/c when it first initializes, it needs to add the instance to the list
        self.picIndex = 0
    def grenadeMovement(self, scrollingDir):
        grenadeMX = 0
        self.collisionRect = pygame.Rect(self.x, self.y, self.w, self.h)
        if scrollingDir == 'left': #moves with the background
            self.x -= 5
        elif scrollingDir == 'right':
            self.x += 5
        #check collision with sprites and platforms and change coordinates accordingly
        if rectCollide(self.collisionRect, rectPlatformList) == True: #if grenade collides with a platform
            rectCollisionList = rectCollideIndexFinder(self.collisionRect, rectPlatformList) 
            grenadeMX = 0 #stops the grenade from moving left/right
            self.y = rectCollisionList[1] - 30
            self.vel_y = 0 #stops the grenade from moving up/down
            self.explosion() #calls the explosion animation
        elif rectCollide(self.collisionRect, rectPlatformList) == False and self.y > HEIGHT :
            self.remove() #if it falls off the screen
        elif self.direction == 'left': #moves left/right depending on where the cat is facing
            grenadeMX -= self.speed
        elif self.direction == 'right':
            grenadeMX += self.speed
        self.vel_y += GRAVITY
        self.x += grenadeMX
        self.y += self.vel_y
    def draw(self):
        if self.explosionAnim == True:
            gameWindow.blit(self.pic, (self.x - 75, self.y - 70)) #displays the explosion animation instead of the grenade
            self.picIndex += 1
        else:
            gameWindow.blit(self.pic, (self.x, self.y))
        if self.removed == False:
            del grenadeRectList[0] #since self.removed is set to True when the grenade is deleted, this has to be done to prevent a list from deleting twice
            grenadeRectList.insert(0, [self.x, self.y, self.w, self.h])
        else:
            grenadeRectList.append([self.x, self.y, self.w, self.h])
            self.removed = False
    def remove(self): 
        del grenadeRectList[0] #the current grenade being deleted is the first one in the list (index 0)
        del grenadeList[0]
        self.removed = True
    def explosion(self):
        self.pic = explosionAnimationList[self.picIndex]
        self.explosionAnim = True
        self.picIndex += 1
        if self.picIndex >= 33:
            self.picIndex = 0
            self.explosionAnim = False
            self.remove()
        
#===================================================================================================================================================================================================

while True:

#GAME STARTING SCREEN: Katelyn ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
  if openingScreen == True and music == True:
    pygame.mixer.init(44100, -16, 2, 2048)
    pygame.mixer.music.load("mainMenuMusic.ogg")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)
    playMusicLoop = False
  elif music == False:
    pygame.mixer.music.stop

  while openingScreen:
    pygame.event.clear()
    nezumiEscapeStartingScreen = pygame.image.load("nezumiEscapeStartingScreen.png")
    gameWindow.blit(nezumiEscapeStartingScreen, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
    if mouseX >= 731 and mouseY <= 67:
        buttons = pygame.mouse.get_pressed()
        if buttons[0]:
            openingScreen = False
            settingScreen = True
            
    keys = pygame.key.get_pressed()
    if keys [pygame.K_SPACE]:
                levelSelect = True
                openingScreen = False

    pygame.display.update()

#SETTING SCREEN: Rosie --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  while settingScreen:
      gameWindow.blit(settingScreenPicture, (221, 47))
      gameWindow.blit(musicControl, (musicControlX, musicControlY))
      for event in pygame.event.get():
          if event.type == pygame.KEYDOWN: 
              if event.key == pygame.K_BACKSPACE:
                  userName = userName[0:-1] #deleting 1 letter from the name by displaying everything but the last index/letter
              else:
                  userName += event.unicode #receiving user input
          if event.type == pygame.MOUSEMOTION:
              mouseX, mouseY = pygame.mouse.get_pos()
      if mouseX >= musicControlX and mouseX <= musicControlX + 29:
          if mouseY >= musicControlY and mouseY <= musicControlY + 27:
              buttons = pygame.mouse.get_pressed()
              if buttons[0]:
                  music = not music #muting/unmuting the music using the toggle button
                  if musicControlX == 440:
                      musicControlX += 35
                  else:
                      musicControlX -= 35
      if mouseX >= backButtonX and mouseX <= backButtonX + 135:
          if mouseY >= backButtonY and mouseY <= backButtonY + 37:
              buttons = pygame.mouse.get_pressed()
              if buttons[0]:
                  settingScreen = False #returning to the openingScreen
                  openingScreen = True
      userNameFont = nameFont.render(userName, 1, WHITE)
      if len(userName) <= 10:
          gameWindow.blit(userNameFont, (411, 324)) #displaying user input
      else:
          userName = userName[0:-1] #setting the maximum character limit to 10
      pygame.display.update()

#LEVEL SELECTION(Katelyn) ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  while levelSelect:
    pygame.event.clear()
    keys = pygame.key.get_pressed()
    nezumiEscapeLevelSelect = pygame.image.load("nezumiEscapeLevelSelect.png")
    nezumiEscapeLevelSelectLocked = pygame.image.load("nezumiEscapeLevelSelectLocked.png")

    if keys [pygame.K_ESCAPE]:
        openingScreen = True
        levelSelect = False

    if forestLevelCompletion == False or beachLevelCompletion == False:
        gameWindow.blit(nezumiEscapeLevelSelectLocked, (0, 0))
    elif forestLevelCompletion == True and beachLevelCompletion == True:
        gameWindow.blit(nezumiEscapeLevelSelect, (0, 0))

    checkMark = pygame.image.load("checkMark.png")
    if beachLevelCompletion == True:
        gameWindow.blit(checkMark, (61, 146))
    if forestLevelCompletion == True:
        gameWindow.blit(checkMark, (438, 146))
    
    buttons = pygame.mouse.get_pressed()
    if buttons[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        if mouseX in range(61, 362) and mouseY in range(145, 321):
            levelChosen = "beach"
            levelSelect = False
            levelsScreen = True
            levelReset = True
        elif mouseX in range(437, 722) and mouseY in range(146, 321):
            levelChosen = "forest"
            levelSelect = False
            levelsScreen = True
            levelReset = True
        elif mouseX in range(249, 551) and mouseY in range(367, 541) and forestLevelCompletion == True and beachLevelCompletion == True:
            levelSelect = False
            gameEndScreen = True
    
    pygame.display.update()



  while levelsScreen:
#LEVEL VARIABLE RESET (Katelyn) ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
    while levelReset == True:
      if levelChosen == "beach": #(Rosie)
        #CAT VARIABLES
        catX = 300 #x has to be less than the scrolling background cutoff, so that it activates the scrolling background, and the black gap is closed
        catY = 300

        #RAT ENEMIES
        ratEnemyRectList = [[0, 520 - ratH, ratW, ratH], [4097, 457 - ratH, ratW, ratH], [1683, 398 - ratH, ratW, ratH]] #UPDATED! (just added one more rat instance here)
        scrollingDir = '' #resetting the scrolling variable for the rat function

        ratIndexList = [0, 1, 2] #this list is used to reset the indexes of the rats since items from the ratEnemyList are being deleted (indexes don't match)

        rat0 = ratEnemy(1355, 520 - ratH, 5, 'right', 0)
        rat1 = ratEnemy(4097, 456 - ratH, 5, 'left', 1)
        rat2 = ratEnemy(2855, 338 - ratH, 5, 'right', 2)

        ratEnemyList = [rat0, rat1, rat2]
        ratEnemyLimitsL = [[1355], [3776], [2855]]
        ratEnemyLimitsR = [[1595], [4097], [3087]]

        #RESETTING POWERUPS (Rosie)
        powerupRectList = [[500, 457 - 45, 50, 50], [2700, 375, 50, 50]]
        grenadeRectList = [] #reset the rectangle list
        grenadeNum = 3 #max grenades
        grenadeList = [] #reset the list here, so grenades disappear once the level restarts
        
        #GENERAL RECTANGLE AND SPRITE LISTS
        beachRectList = [[0, 480, 395, 160], [395, 457, 400, 160], [954, 460, 400, 160], [1355, 520, 240, 160], [1975, 520, 240, 160], [3374, 520, 400, 160], [3774, 457, 320, 160], [813, 280, 116, 58], [1683, 398, 232, 58], [2342, 377, 116, 58], [2579, 420, 174, 58], [2855, 338, 232, 58], [3222, 270, 58, 58], [4243, 335, 174, 58]]
        #for rectangle collision, the rectangles should not overlap (eg. before the first rect had a width of 400, but the next rectangle x was at 395.. created errors)                               
        beachSpriteListPlatforms = [[0, 480, terrain5x2], [395, 457, terrain5x2], [954, 460, terrain5x2], [1353, 520, terrain3x2], [1975, 520, terrain3x2], [3374, 520, terrain5x2], [3774, 457, terrain4x2], [813, 280, crate2x1], [1683, 398, crate4x1], [2342, 377, crate2x1], [2579, 420, crate3x1], [2855, 338, crate4x1], [3222, 270, crate1x1], [4243, 335, crate3x1]]
        beachSpriteListDecor = [[-46, 281, bigTree2],  [274, 451, mushroomShort], [293, 451, mushroomMed], [328, 421, woodSign],  [1179, 430, mushroomMed], [1199, 430, mushroomTall], [1204, 304, bigTree1], [1288, 430, coral], [2140, 448, rockArrows], [2356, 348, mushroomShort], [3407, 374, smallTree],  [3723, 492, mushroomShort], [3539, 482, sandCastle]]        

        #DEADLY OBSTABLES LIST
        beachSpriteDeadlySpikes = [[731, 426, spikes2], [953, 428, spikes3], [3673, 490, spikes3]]
        beachRectSpikes = [[740, 426, 55, 34], [953, 428, 86, 33], [3685, 490, 83, 33]] #making the hitboxes a bit more generous
        
        #END OF LEVEL PORTAL
        levelPortal = pygame.image.load('beachPortal.png')
        levelPortalSprite = [[4500, 113, levelPortal]]
        levelPortalRect = [[4500, 113, 198, 358]]

        #COLLECTIVE LISTS AND LIST GENERAL VARIABLE RESET (to be the same as in second part of loop)
        rectPlatformList = beachRectList
        deadlyObstaclesList = beachRectSpikes
        spriteList = [beachSpriteListPlatforms, beachSpriteListDecor, beachSpriteDeadlySpikes, levelPortalSprite]
        rectShiftList = [rectPlatformList, deadlyObstaclesList, ratEnemyRectList, levelPortalRect]

        #SCROLLING BACKGROUND
        levelBackground1 = lvl_1_Background
        levelBackground2 = lvl_1_BackgroundFlip
        levelBackground1W = 800
        levelBackground1X = 5 #if you set it to 5, there's not weird background glitch because it doesn't overlap showing the characters from previous frams
        levelBackground1Y = 0
        levelBackground2W = 800
        levelBackground2X = 800
        levelBackground2Y = 0
        levelBackgroundMove = 5
        scrollingBgCutoff = 400

        #RESETTING GENERAL VARIABLES WHEN LEVEL FIRST STARTS: If variables are not set in the if-statements, level selection screen won't work (Katelyn)
        lastMove = "none"
        catReset = "none"
        air = True
        levelReset = False
        rectCollisionListUp = ["none"]
        rectCollisionListDown = ["none"]
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

      elif levelChosen == "forest": #(Katelyn)
        #CAT VARIABLES
        catX = 400
        catY = 400
        catJump = -30

        #RAT ENEMIES (Rosie)
        ratEnemyRectList = [[500, 480 - ratH, ratW, ratH], [1191, 407 - ratH, ratW, ratH], [2090, 339 - ratH, ratW, ratH], [3035, 480 - ratH, ratW, ratH], [3548, 480 - ratH, ratW, ratH], [3936, 541 - ratH, ratW, ratH],
        [4426, 541 - ratH, ratW, ratH], [5329, 480 - ratH, ratW, ratH]]
        scrollingDir = '' #resetting the scrolling variable for the rat function

        ratIndexList = [0, 1, 2, 3, 4, 5, 6, 7] 

        rat0 = ratEnemy(ratEnemyRectList[0][0], ratEnemyRectList[0][1], 5, 'right', 0)
        rat1 = ratEnemy(ratEnemyRectList[1][0], ratEnemyRectList[1][1], 5, 'left', 1)
        rat2 = ratEnemy(ratEnemyRectList[2][0], ratEnemyRectList[2][1], 3, 'left', 2)
        rat3 = ratEnemy(ratEnemyRectList[3][0], ratEnemyRectList[3][1], 5, 'right', 3)
        rat4 = ratEnemy(ratEnemyRectList[4][0], ratEnemyRectList[4][1], 5, 'left', 4)
        rat5 = ratEnemy(ratEnemyRectList[5][0], ratEnemyRectList[5][1], 5, 'right', 5)
        rat6 = ratEnemy(ratEnemyRectList[6][0], ratEnemyRectList[6][1], 5, 'left', 6)
        rat7 = ratEnemy(ratEnemyRectList[7][0], ratEnemyRectList[7][1], 5, 'left', 7)
        
        ratEnemyList = [rat0, rat1, rat2, rat3, rat4, rat5, rat6, rat7]
        ratEnemyLimitsL = [[500], [1191], [2090], [3035], [3548], [3936], [3936], [5329]]
        ratEnemyLimitsR = [[800], [1396], [2292], [3411], [3921], [4426], [4426], [5479]]    

        #RESETTING POWERUPS (Rosie)
        #adsfkajsdklfjaskdfj

        #RECTANGLE LISTS AND SPRITE LISTS
        forestRectList = [[0, 541, 480, 59], [480,480, 319, 120], [828, 320, 126, 45], [993, 258, 166, 45], [1191, 407, 206, 45],   [1286, 204, 126, 45], [1527, 280, 86, 45], [1726, 280, 126, 45], [1890, 200, 166, 45], [2090, 339, 206, 45], [2426, 221, 86, 45], [2650, 259, 166, 45], [2850, 206, 126, 45], [3020, 480, 912, 120], [3917, 541, 660, 59], [4687, 401, 126, 45], [4926, 480, 176, 120], [5321, 480, 176, 120],  [5605, 541, 1454, 59], [5172, 405, 86, 45]]
        deadlyObstaclesList = [[909, 286, 24, 34], [1337, 171, 24, 34], [2932, 172, 24, 34], [5764, 508, 95, 33]]

        forestSpriteListPlatforms = [[0, 541, forestBlock3x1x3], [480, 480, forestBlock3x2x2], [828, 320, woodBlock3x1], [993, 258, woodBlock4x1], [1191, 407, woodBlock5x1], [1286, 204, woodBlock3x1], [1527, 280, woodBlock2x1], [1726, 280, woodBlock3x1], [1890, 200, woodBlock4x1], [2090, 339, woodBlock5x1], [2426, 221, woodBlock2x1], [2650, 259, woodBlock4x1], [2850, 206, woodBlock3x1], [3020, 480, forestBlock3x2x2], [3317, 480, forestBlock3x2x2], [3613, 480, forestBlock3x2x2], [3917, 541, forestBlock3x1], [4075, 541, forestBlock3x1], [4237, 541, forestBlock3x1], [4395, 541, forestBlock3x1],  [4687, 401, woodBlock3x1], [4926, 480, forestBlock3x2], [5321, 480, forestBlock3x2], [5605, 541, forestBlock3x1x3], [6083, 541, forestBlock3x1x3], [6561, 541, forestBlock3x1x3], [5172, 405, woodBlock2x1]]
        forestSpriteListDecor = [[791, 480, forestWater], [1348, 480, forestWater], [1908, 480, forestWater], [2467, 480, forestWater], [760, 427, sign1], [570, 461, flower2], [3174, 461, flower2], [4535, 523, flower2], [5711, 522, flower2],
        [6084, 518, flower1], [3937, 518, flower1], [3525, 457, flower1], [40, 510, fence1], [160, 510, fence1], [3030, 449, fence1], [5927, 510, fence1], [6665, 496, sign2]]
        deadlyObtaclesSpriteList = [[889, 286, spikes2], [1317, 171, spikes2], [2912, 172, spikes2], [5764, 508, spikes3]]

        #END OF LEVEL PORTAL
        levelPortal = pygame.image.load('forestPortal.png')
        levelPortalSprite = [[6800, 88, levelPortal]]
        levelPortalRect = [[6800, 88, 247, 421]]

        #MAIN COLLECTIVE LISTS
        rectPlatformList = forestRectList
        spriteList = [forestSpriteListPlatforms, forestSpriteListDecor, deadlyObtaclesSpriteList, levelPortalSprite]
        rectShiftList = [rectPlatformList, deadlyObstaclesList, ratEnemyRectList, levelPortalRect]

        rectSlimeList = [[735, 440, 58, 41]]

        #SCROLLING BACKGROUND VARIABLES
        levelBackground1 = forestBackground1
        levelBackground2 = forestBackground2
        levelBackground1W = 1190
        levelBackground1X = 0
        levelBackground1Y = 0
        levelBackground2W = 1190
        levelBackground2X = 1190
        levelBackground2Y = 0
        levelBackgroundMove = 5
        scrollingBgCutoff = 400    

        #RESETTING GENERAL VARIABLES WHEN LEVEL FIRST STARTS: If variables are not set in the if-statements, level selection screen won't work (Katelyn)
        lastMove = "none"
        catReset = "none"
        air = True
        levelReset = False
        rectCollisionListUp = ["none"]
        rectCollisionListDown = ["none"]

#START OF PLAYING LEVEL ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
    pygame.event.clear()
    pygame.time.delay(10)
    keys = pygame.key.get_pressed()

    if keys [pygame.K_ESCAPE]:
        levelSelect = True
        levelsScreen = False
        
    #DRAWING SCROLLING BACKGROUND AND SETTING CAT (Katelyn)
    scrollingBackground(levelBackground1, levelBackground2)
    catRect = pygame.Rect(catX + 20, catY, catW, catH)
    rectCollision = rectCollide(catRect, rectPlatformList)

    #IF CAT KILLS RATS WITH GRENADES (Rosie)
    if len(grenadeList) > 0:
        if rectCollide(pygame.Rect(grenadeRectList[0]), ratEnemyRectList) == True:
            index = ratEnemyRectList.index(rectCollideIndexFinder(pygame.Rect(grenadeRectList[0]), ratEnemyRectList)) #finds the index of the rat that the grenade collides with
            del ratEnemyList[index] #deletes that index from all of these lists
            del ratEnemyRectList[index]
            del ratIndexList[index]
            del ratEnemyLimitsL[index]
            del ratEnemyLimitsR[index]   

    #CREATE RATS (Rosie)
    for rat in ratEnemyList:
        rat.movement(ratEnemyLimitsL, ratEnemyLimitsR, scrollingDir)
        rat.draw()

    #DRAWING POWERUPS
    for i in range(len(powerupRectList)):
        gameWindow.blit(grenadePickup, (powerupRectList[i][0], powerupRectList[i][1]))

    #DRAWING SPRITES (Katelyn)
    for i in range(len(spriteList)):
        drawSprites(spriteList[i])

    #MOVEMENT USING KEYS: Cat Sprites (Rosie), Cat Collision (Katelyn)
    if keys [pygame.K_d] and catReset != "right" and (rectCollision == False or lastMove != "right"):
        catX += catMX
        if air == False:
            lastMove = "right"
            catReset = "none"
            catPicIndex += 1
    elif keys [pygame.K_a] and catReset != "left" and (rectCollision == False or lastMove != "left"):
        catX -= catMX
        if air == False:
            lastMove = "left"
            catReset = "none"
            catPicIndex += 1
    else:
        if lastMove == "right":
            catPicIndex = 0
        if lastMove == "left":
            catPicIndex = 0
        if lastMove == "up" and air == False:
            if jumpDir == "right":
                catPicIndex = 0
            else:
                catPicIndex = 2
        
    if keys [pygame.K_w] and air == False and (rectCollision == False or lastMove != "up"):
        if lastMove == "right":
            catPicIndex = 1
            lastMove = "up"
            jumpDir = "right"
        elif lastMove == "left":
            catPicIndex = 3
            lastMove = "up"
            jumpDir = "left"
        elif lastMove == "up":
            catPicIndex = 0
            lastMove = "up"
        catMY = catJump
        catReset = "none"
        air = True
        rectCollisionUpUse = 0

    if catPicIndex > 18:
        catPicIndex = 0

    #ACTIVATING THE GRENADES
    if len(grenadeList) == 0: #we only want the player to throw one grenade at a time
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: #keydown so that the player cannot hold the button down and repetively throw grenades
                if event.key == pygame.K_SPACE:
                    if grenadeActivation == True and grenadeNum > 0: #the player has a total of 3 shots
                        grenade = grenadePowerup(catX + catW, catY, 5, lastMove, grenadeImg)
                        grenadeList.append(grenade)
                    grenadeNum -= 1

    if grenadeActivation:
        grenadeCounter(grenadeNum) #display the amount of grenades the player has
        #calls the movement and the drawing functions
        for grenade in grenadeList:
            grenade.draw()
            grenade.grenadeMovement(scrollingDir)

    #IF CAT PICKS UP POWERCUBE
    if rectCollide(catRect, powerupRectList) == True:
        powerupRectList.remove(rectCollideIndexFinder(catRect, powerupRectList)) #stops displaying the sprite
        grenadeActivation = True
        grenadeNum = 3 #refill grenades     

    #IF CAT FALLS OFF PLATFORM: RESULTS IN GRAVITY (Katelyn)
    if rectCollisionListDown != ["none"]:
        if catX > rectCollisionListDown[0] + rectCollisionListDown[2] and lastMove or catX + catW < rectCollisionListDown[0]:
            air = True

    #IF CAT IS NOT ON ANY PLATFORM: RESULTS IN GRAVTY (Katelyn)
    inAir = 0
    for i in range(len(rectPlatformList)): 
        if catX + catW < rectPlatformList[i][0] or catX > rectPlatformList[i][0] + rectPlatformList[i][2]:
            inAir += 1
        if inAir == len(rectPlatformList):
            air = True

    #IF CAT IS IN THE AIR: GRAVITY IS APPLIED (Katelyn)
    if air == True:
        catMY += GRAVITY
        catY += catMY

    #IF CAT COLLIDES WITH A RECTANGLE: RESETS COORDINATES TO MAKE IT EXACTLY ABOVE OR BESIDE RECT (Katelyn)
    if rectCollide(catRect, rectPlatformList) == True: #If cat collides with a platform
        rectCollisionList = rectCollideIndexFinder(catRect, rectPlatformList) #tracks the rectangle information that the car collides with
        rectCollisionX = rectCollisionList[0]
        rectCollisionY = rectCollisionList[1]
        rectCollisionW = rectCollisionList[2]
        rectCollisionH = rectCollisionList[3]

        if air == True and catY + catH > rectCollisionY and (catX in range(rectCollisionX, rectCollisionX + rectCollisionW) or catX + catW in range(rectCollisionX, rectCollisionX + rectCollisionW)) and catMY < 0: #Fore reseting cat to ground level
            catY = rectCollisionY + rectCollisionH #Sets cat to bottom of block
            rectCollisionListUp = rectCollisionList
        else:
            rectCollisionListUp = ["none"]

        if air == True and (rectCollisionListUp == ["none"] or catRect.colliderect(rectCollisionListUp) == False) and (catX in range(rectCollisionX, rectCollisionX + rectCollisionW) or catX + catW in range(rectCollisionX, rectCollisionX + rectCollisionW)): #Fore reseting cat to ground level
            catY = rectCollisionY - catH
            air = False
            catReset = "down"
            catMY = 0
            rectCollisionListDown = rectCollisionList
        else:
            rectCollisionListDown = ["none"]
            
        if lastMove == "right" and catX + catW > rectCollisionX and catX < rectCollisionX - catW/2: #Reseting cat coordinates when colliding with right
            for i in range (catY, catY + catH):
                if i in range(rectCollisionY, rectCollisionY + rectCollisionH):     
                    catX = rectCollisionX - catW
                    catReset = "right"
                    
        elif lastMove == "left" and catX < rectCollisionX + rectCollisionW and catX + catW > rectCollisionX + rectCollisionW + catW/2:#Reseting cat coordinates when colliding with Left
            for i in range (catY, catY + catH):
                if i in range(rectCollisionY, rectCollisionY + rectCollisionH):  
                    catX = rectCollisionX + rectCollisionW
                    catReset = "left"

    #SCROLLING BACKGROUND CHARACTER MOVES RIGHT (Rosie)
    if catX > scrollingBgCutoff:
        catX = scrollingBgCutoff
        levelBackground1X -= levelBackgroundMove
        if levelBackground1X <= -levelBackground1W:
            levelBackground1X = levelBackground1W
        levelBackground2X -= levelBackgroundMove
        if levelBackground2X <= -levelBackground2W:
            levelBackground2X = levelBackground2W
            
        for i in range(len(rectShiftList)): #(Katelyn)
          rectShiftList[i] = itemShift(rectShiftList[i], -5)
          
        for i in range(len(spriteList)): #(Katelyn)
          spriteList[i] = itemShift(spriteList[i], -5)

        for i in range(len(ratEnemyLimitsL)): #(Rosie)
            ratEnemyLimitsL[i][0] -= 5  #shifting the limits of the rat to the left
            ratEnemyLimitsR[i][0] -= 5
            
        for i in range(len(powerupRectList)):
            powerupRectList[i][0] -= 5
        scrollingDir = 'left'
        
    #SCROLLING BACKGROUND CHARACTER MOVES LEFT (Rosie)
    elif catX < 400 - 20:
        catX = 400 - 20
        levelBackground1X += levelBackgroundMove
        if levelBackground1X >= levelBackground1W:
            levelBackground1X = -levelBackground1W
        levelBackground2X += levelBackgroundMove
        if levelBackground2X >= levelBackground2W:
            levelBackground2X = -levelBackground2W

        for i in range(len(rectShiftList)): #(Katelyn)
          rectShiftList[i] = itemShift(rectShiftList[i], 5)
          
        for i in range(len(spriteList)): #(Katelyn)
          spriteList[i] = itemShift(spriteList[i], 5)
          
        for i in range(len(ratEnemyLimitsL)): #(Rosie)
            ratEnemyLimitsL[i][0] += 5  #shifting the limits of the rat to the right
            ratEnemyLimitsR[i][0] += 5

        for i in range(len(powerupRectList)): #(Rosie)
            powerupRectList[i][0] += 5 #shifting the powerup cubes
        scrollingDir = 'right' #used for the rat and grenade functions
    else:
        scrollingDir = ''  

    #IF CAT DIES >:( (Collab)
    if catY + catH > HEIGHT and air == True: #Player falls off platform and out of the screen
        catMEow.play(0)
        levelReset = True
    if rectCollide(catRect, ratEnemyRectList) == True:
        catMEow.play(0)
        levelReset = True
    if rectCollide(catRect, deadlyObstaclesList) == True:
        catMEow.play(0)
        levelReset = True

    #IF CAT SUCCEEDS :)) (Collab)
    if rectCollide(catRect, levelPortalRect) == True:
        if levelChosen == "beach":
            beachLevelCompletion = True
        elif levelChosen == "forest":
            forestLevelCompletion = True
        levelsScreen = False
        levelSelect = True
        
    gameWindow.blit(catAnimation(lastMove), (catX, catY - 12))
    pygame.display.update()

#-------------------------------------------------------------------------------------------------------------------------------------------------
  while gameEndScreen:
      pygame.event.clear()
      nezumiEscapeEndingScreen = pygame.image.load("nezumiEscapeEndingScreen.png")
      gameWindow.blit(nezumiEscapeEndingScreen, (0,0))
      keys = pygame.key.get_pressed()
      
      if keys [pygame.K_ESCAPE]:
          pygame.quit()
          
      pygame.display.update()
      

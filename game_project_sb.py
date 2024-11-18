import pygame
import sys
from pygame.locals import QUIT
import random
import math
from player_class import player
from player_class import Directions
from gun_class import GunLogic

pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("death commando: pest control")
clock = pygame.time.Clock()

playing = False
mainMenu = True
guideMenu = False

waveStop = True

#plane color surfaces
white_line = pygame.Surface((60,7.5))
white_line.fill("white")

bullet_cube = pygame.Surface((50,65))
bullet_cube.fill("white")
boxCoordX = 820
boxCoordY = 615

plane = pygame.Surface((60,60))
plane.fill("blue")
planeRect = plane.get_rect()
# Load images
background = pygame.image.load("x/background.png")
guide1 = pygame.image.load("x/guide1.png")


enemy_1 = pygame.image.load("x/enemy_1.png").convert_alpha()
enemy_1 = pygame.transform.rotate(enemy_1, 90)
enemy_1 = pygame.transform.scale(enemy_1, (60, 60))

enemy_2 = pygame.image.load("x/enemy_2.png").convert_alpha()
enemy_2 = pygame.transform.rotate(enemy_2, 90)
enemy_2 = pygame.transform.scale(enemy_2, (60, 60))

brute_1 = pygame.image.load("x/brute_1.png").convert_alpha()
brute_1 = pygame.transform.rotate(brute_1, 90)
brute_1 = pygame.transform.scale(brute_1, (90, 90))

brute_2 = pygame.image.load("x/brute_2.png").convert_alpha()
brute_2 = pygame.transform.rotate(brute_2, 90)
brute_2 = pygame.transform.scale(brute_2, (90, 90))

rager_1 = pygame.image.load("x/rager_1.png")
rager_1 = pygame.transform.rotate(rager_1, 90)
rager_1 = pygame.transform.scale(rager_1, (70, 70))

rager_2 = pygame.image.load("x/rager_2.png")
rager_2 = pygame.transform.rotate(rager_2, 90)
rager_2 = pygame.transform.scale(rager_2, (70, 70))

burster_1 = pygame.image.load("x/burster_1.png")
burster_1 = pygame.transform.rotate(burster_1, 90)
burster_1 = pygame.transform.scale(burster_1, (70, 70))

burster_2= pygame.image.load("x/burster_2.png")
burster_2 = pygame.transform.rotate(burster_2, 90)
burster_2 = pygame.transform.scale(burster_2, (70, 70))

menuEnemy_1 = pygame.transform.rotate(enemy_1, 270)
menuEnemy_2 = pygame.transform.rotate(enemy_2, 270)

menuEnemySprites = [menuEnemy_1,menuEnemy_2]

menuBrute_1 = pygame.transform.rotate(brute_1, 270)
menuBrute_2 = pygame.transform.rotate(brute_2, 270)

menuBruteSprites = [menuBrute_1,menuBrute_2]

menuRager_1 = pygame.transform.rotate(rager_1, 270)
menuRager_2 = pygame.transform.rotate(rager_2, 270)

menuRagerSprites = [menuRager_1,menuRager_2]

player_frame_1 = pygame.image.load("x/player_1.png").convert_alpha()
player_frame_1 = pygame.transform.rotate(player_frame_1, 90)
player_rect = player_frame_1.get_rect()

player_shoot_1 = pygame.image.load("x/player_shoot_1.png").convert_alpha()
player_shoot_1 = pygame.transform.rotate(player_shoot_1, 90)

player_shoot_2 = pygame.image.load("x/player_shoot_2.png").convert_alpha()
player_shoot_2 = pygame.transform.rotate(player_shoot_2, 90)

player_shoot_3 = pygame.image.load("x/player_shoot_3.png").convert_alpha()
player_shoot_3 = pygame.transform.rotate(player_shoot_3, 90)

playerMK2_1 = pygame.image.load("x/player_MK2_1.png").convert_alpha()
playerMK2_1 = pygame.transform.rotate(playerMK2_1, 90)

playerMK2_shoot_1 = pygame.image.load("x/player_MK2shoot_1.png").convert_alpha()
playerMK2_shoot_1 = pygame.transform.rotate(playerMK2_shoot_1, 90)

playerMK2_shoot_2 = pygame.image.load("x/player_MK2shoot_2.png").convert_alpha()
playerMK2_shoot_2 = pygame.transform.rotate(playerMK2_shoot_2, 90)

playerMK2_shoot_3 = pygame.image.load("x/player_MK2shoot_3.png").convert_alpha()
playerMK2_shoot_3 = pygame.transform.rotate(playerMK2_shoot_3, 90)

playerSMG_1 = pygame.image.load("x/player_SMG_1.png").convert_alpha()
playerSMG_1 = pygame.transform.rotate(playerSMG_1, 90)

playerSMG_shoot_1 = pygame.image.load("x/player_SMGshoot_1.png").convert_alpha()
playerSMG_shoot_1 = pygame.transform.rotate(playerSMG_shoot_1, 90)

playerSMG_shoot_2 = pygame.image.load("x/player_SMGshoot_2.png").convert_alpha()
playerSMG_shoot_2 = pygame.transform.rotate(playerSMG_shoot_2, 90)

playerSMG_shoot_3 = pygame.image.load("x/player_SMGshoot_3.png").convert_alpha()
playerSMG_shoot_3 = pygame.transform.rotate(playerSMG_shoot_3, 90)

playerFLEX_1 = pygame.image.load("x/player_FLEX_1.png").convert_alpha()
playerFLEX_1 = pygame.transform.rotate(playerFLEX_1, 90)

playerFLEX_shoot_1 = pygame.image.load("x/player_FLEX_shoot1.png").convert_alpha()
playerFLEX_shoot_1 = pygame.transform.rotate(playerFLEX_shoot_1, 90)

playerFLEX_shoot_2 = pygame.image.load("x/player_FLEX_shoot2.png").convert_alpha()
playerFLEX_shoot_2 = pygame.transform.rotate(playerFLEX_shoot_2, 90)

playerFLEX_shoot_3 = pygame.image.load("x/player_FLEX_shoot3.png").convert_alpha()
playerFLEX_shoot_3 = pygame.transform.rotate(playerFLEX_shoot_3, 90)

terror_logo = pygame.image.load("x/terror_crops_logo.png")
terror_logo = pygame.transform.scale(terror_logo, (40, 40))

bulletUI = pygame.image.load("x/bulletUI.png")
bulletUI = pygame.transform.scale(bulletUI, (200, 100))

ammo1 = pygame.image.load("x/ammo_1.png")
ammo1 = pygame.transform.scale(ammo1, (150, 100))
ammoMask = pygame.mask.from_surface(ammo1)

ammo2 = pygame.image.load("x/ammo_2.png")
ammo2 = pygame.transform.scale(ammo2, (150, 100))

ammo3 = pygame.image.load("x/ammo_3.png")
ammo3 = pygame.transform.scale(ammo3, (150, 100))

ammoAnimationList = [ammo1,ammo2,ammo3,ammo2,ammo1]

drop1 = pygame.image.load("x/drop1.png")
drop1 = pygame.transform.scale(drop1, (125, 125))

drop2 = pygame.image.load("x/drop2.png")
drop2 = pygame.transform.scale(drop2, (125, 125))

drop3 = pygame.image.load("x/drop3.png")
drop3 = pygame.transform.scale(drop3, (125, 125))

drop4 = pygame.image.load("x/drop4.png")
drop4 = pygame.transform.scale(drop4, (125, 125))

dropAnimationList = [drop1,drop2,drop3,drop4]

medPack1 = pygame.image.load("x/medPack1.png")
medPack1 = pygame.transform.scale(medPack1, (150, 100))
medPackMask = pygame.mask.from_surface(medPack1)

medPack2 = pygame.image.load("x/medPack2.png")
medPack2 = pygame.transform.scale(medPack2, (150, 100))

medPack3 = pygame.image.load("x/medPack3.png")
medPack3 = pygame.transform.scale(medPack3, (150, 100))

medPackAnimationList = [medPack1,medPack2,medPack3,medPack2,medPack1]

callInUI = pygame.image.load("x/callInUI.png") #scale: 112 by 79
callInUI = pygame.transform.scale(callInUI, (350, 175))

gameLogo = pygame.image.load("x/mainMenu.png")

playButton1 = pygame.image.load("x/playButton1.png")
playButtonRect = playButton1.get_rect()
playButtonRect.topleft = (82,535)

guideButtonRect = playButton1.get_rect()
guideButtonRect.topleft = (512,535)

playButtonMask = pygame.mask.from_surface(playButton1)

playButtonState = playButton1

playButton2 = pygame.image.load("x/playButton2.png")

crosshair = pygame.image.load("x/crosshair.png")
crosshair = pygame.transform.scale(crosshair, (50, 50))
cursor = pygame.cursors.Cursor((0,0), crosshair)
pygame.mouse.set_cursor(cursor)

gun_shoot = pygame.mixer.Sound("sounds/gunShoot.mp3")
gun_shoot.set_volume(0.15)

gun_Close = pygame.mixer.Sound("sounds/gunClose.wav")
gun_Close.set_volume(2)
gun_Reload = pygame.mixer.Sound("sounds/gunReload.wav")
gun_Reload.set_volume(1.2)
gun_Open = pygame.mixer.Sound("sounds/gunOpen.wav")
gun_Open.set_volume(2)
smgShoot = pygame.mixer.Sound("sounds/smgShoot.wav")
smgShoot.set_volume(4)

enemy_death = pygame.mixer.Sound("sounds/enemy_death.wav")
enemy_death.set_volume(0.25)

enemy1 = pygame.mixer.Sound("sounds/enemy1.wav")
enemy1.set_volume(0.25)

bruteDeath = pygame.mixer.Sound("sounds/enemy2.wav")
bruteDeath.set_volume(0.25)

ragerDeath = pygame.mixer.Sound("sounds/enemy1.wav")
ragerDeath.set_volume(0.5)

shop_refuse = pygame.mixer.Sound("sounds/shop_refuse.wav")
shop_happy = pygame.mixer.Sound("sounds/shop_happy.wav")

supplyDropAlert = pygame.mixer.Sound("sounds/supplyDrop.wav")
hordeAlert = pygame.mixer.Sound("sounds/hordeAlert.wav")
hordeAlert2 = pygame.mixer.Sound("sounds/hordeAlert2.wav")
hordeAlert3 = pygame.mixer.Sound("sounds/hordeAlert3.wav")
hordeAlert4 = pygame.mixer.Sound("sounds/hordeAlert4.wav")
hordeAlert5 = pygame.mixer.Sound("sounds/hordeAlert5.wav")

breakAlert = pygame.mixer.Sound("sounds/breakAlert.wav")

FLEXShoot = pygame.mixer.Sound("sounds/FLEXshoot.wav")
FLEXShoot.set_volume(2.5)

rifleShot = pygame.mixer.Sound("sounds/rifleShot.wav")
rifleShot.set_volume(0.4)

metalReload1 = pygame.mixer.Sound("sounds/metalReload1.wav")
metalReload1.set_volume(4.5)

metalReload2 = pygame.mixer.Sound("sounds/metalReload2.wav")
metalReload2.set_volume(4.5)

metalReload3 = pygame.mixer.Sound("sounds/metalReload3.wav") #credit: marb7e
metalReload3.set_volume(4.5)

hordeAlertList = [hordeAlert,hordeAlert2,hordeAlert3,hordeAlert4,hordeAlert5]

music = pygame.mixer.Sound("sounds/placeholder.mp3")
music.set_volume(15)

HL_font = pygame.font.Font("fonts/Swiss 721 Extended Bold.otf", 30)

#player input
R_pressed = False
M_pressed = False
Space_pressed = False
E_pressed = False
N_pressed = False
P_pressed = False
T_pressed = False
pressed_1 = False
pressed_3 = False
ESC_pressed = False

#frame data
current_frame = 0
frame_offset = 0
Frame_checker = 0
player_frame_offest = 0
WeaponSwapFrame = False
ammoFrame = 0
ammoFrame2 = 0
resupFlareFrame = 0
resupFlareFrame2 = 0
medPackAnimationFrame = 0
lastFrameNotFired = 0
MenuFrame = 0
menuFrame_offset = 0

bruteSpawnTime = 400
ragerSpawnTime = 220
bursterSpawnTime = 280
enemySpawnTime = 35
maxEnemies = 40

#shop data
coin = 1
restockPrice = 75
resupCallFrame = 0
resupCalledIn = False

medPackCallFrame = 0
medPackCalledIn = False
medPackPrice = 10
medPackRestock = False

coin_display = str(coin)

shopTest = False
resupBlit = False

ammoShopBuy = False
ammoRestock = False

#player data
player_rect.x = 400
player_rect.y = 250
MoveSpeed = 1.2
dashCooldown = 90

playerHealth = 50

current_player_frame = player_frame_1

playerSpriteList = []

MK1ravagerList = [player_frame_1,player_shoot_1,player_shoot_2,player_shoot_3]
MK2ravagerList = [playerMK2_1,playerMK2_shoot_1,playerMK2_shoot_2,playerMK2_shoot_3]
SMGList = [playerSMG_1,playerSMG_shoot_1,playerSMG_shoot_2,playerSMG_shoot_3]
FLEXList = [playerFLEX_1,playerFLEX_shoot_1,playerFLEX_shoot_2,playerFLEX_shoot_3]

#enemy data
enemy_speed = 1.4  # pixels per frame?
enemyHealth = 5

enemyDamage = 3
enemyHitCooldown = 0
enemyCooldown = 90
enemyHitTimer = False

chainsaw_animation_list = [enemy_1, enemy_2]
enemy_Xlist = []
enemy_Ylist = []
enemyHealthList = []

menuEnemy_Xlist = []
menuEnemy_Ylist = []

CanSpawnEnemy = True
Enemy_Clipped_line = False
enemyHitPlayer = False

currentEnemyWave = 1

#brute data
bruteSpeed = 0.5
bruteHealth = 75
bruteChargeSpeed = 1

bruteDamage = 10
bruteHitCooldown = 0
bruteCooldown = 180
bruteHitPlayer = False
bruteHitTimer = False

bruteAnimationList = [brute_1,brute_2]
bruteHealthList = []
bruteXList = []
bruteYList = []
menuBrute_Xlist = []
menuBrute_Ylist = []
bruteSpeedList = []


bruteClippedLine = False

#rager data
ragerSpeed = 3.5
ragerHealth = 12.5

ragerDamage = 1
ragerHitCooldown = 0
ragerCooldown = 60
ragerHitPlayer = False

ragerAnimationList = [rager_1,rager_2]
ragerHealthList = []
ragerXList = []
ragerYList = []
menuRager_Xlist = []
menuRager_Ylist = []

ragerClippedLine = False

#burster data
bursterSpeed = 1.5
bursterHealth = 5

bursterAnimationList = [burster_1,burster_2]
bursterHealthList = []
bursterXList = []
bursterYList = []

bursterClippedLine = False

#weapon data
damage = 5
Total_Ammo = 0
Firerate = 6 # frames per shot
magSize = 35

shootSound = gun_shoot

MK1ReloadList = [0,35,80]

MK2ReloadList = [0,45,90]

SMGReloadList = [0,20,40]

FLEXReloadList = [0,25,45]

metalReloadList = [metalReload1,metalReload2,metalReload3]

classicReloadList = [gun_Open,gun_Reload,gun_Close]

ammo = magSize
ammoSize = ammo

Gun_already_fired = False
Is_reloading = False
WeaponSwapFrame = True

currentGun = "flex"

reloadList = [gun_Open, gun_Reload, gun_Close]
WeaponList = []

gun_firing_frame = False # gun active
CanShoot = False
OutOfAmmo = False

ammo_display = str(ammo)
Total_Ammo_display = str(Total_Ammo)
playerHealthDis = str(playerHealth)

WHITE = (0, 0, 0)

Current_Direction = Directions.InValid
p1 = player(Current_Direction,Space_pressed,current_frame,dashCooldown)
g1 = GunLogic(M_pressed,Firerate,current_frame,Enemy_Clipped_line,Gun_already_fired,Is_reloading)

def gradient_text(surface, text, font, color_start, color_end, position):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(topleft=position)
    gradient_surface = pygame.Surface(text_rect.size, pygame.SRCALPHA)
    for x in range(text_rect.width):
        ratio = x / text_rect.width
        r = int(color_start[0] * (1 - ratio) + color_end[0] * ratio)
        g = int(color_start[1] * (1 - ratio) + color_end[1] * ratio)
        b = int(color_start[2] * (1 - ratio) + color_end[2] * ratio)
        pygame.draw.line(gradient_surface, (r, g, b), (x, 0), (x, text_rect.height))
    gradient_surface.blit(text_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    surface.blit(gradient_surface, text_rect.topleft)

def GetRotationAngle(playerCoords,coordList):
    rotX = playerCoords.x - coordList[0]
    rotY = playerCoords.y - coordList[1]
    angle_radians = math.atan2(rotY, rotX) 
    angle_degrees = math.degrees(angle_radians)
    return [rotX,rotY,angle_degrees]

def MoveEnemyX(rotX,rotY,currentX,speed):
    dist = math.hypot(rotX, rotY) or 0.000001
    dirX = rotX / dist
    currentX += dirX * speed
    return currentX

def MoveEnemyY(rotX,rotY,currentY,speed):
    dist = math.hypot(rotX, rotY) or 0.000001
    dirY = rotY / dist
    currentY += dirY * speed
    return currentY

def CheckWeapon(Weapon):
    if (Weapon == "MK1ravager"):
        return [5,150,25,6,MK1ravagerList,MK1ReloadList,rifleShot,50,1,classicReloadList] #damage, total ammo, mag size, fire rate, player sprites list, reload times, shoot sound, resup cost, audio handling, reload sounds
    elif (Weapon == "MK2ravager"):
        return [5,300,50,3,MK2ravagerList,MK2ReloadList,rifleShot,200,2,classicReloadList] #damage, total ammo, mag size, fire rate, player sprites list, reload times, shoot sound, resup cost, audio handling, reload sounds
    elif (Weapon == "SMG"):
        return [1.5,0,425,1,SMGList,SMGReloadList,smgShoot,150,1,classicReloadList] #damage, total ammo, mag size, fire rate, player sprites list, reload times, shoot sound, resup cost, audio handling, reload sounds
    elif (Weapon == "flex"):
        return [5,150,25,15,FLEXList,FLEXReloadList,FLEXShoot,75,1,metalReloadList] #damage, total ammo, mag size, fire rate, player sprites list, reload times, shoot sound, resup cost, audio handling, reload sounds
    
def enemyCol(enemy):
    if pygame.Rect.colliderect(enemy,playerRoatedRect):
        return True
    else:
        return False

def Animation(current_frame,maxFrames,inputFrame,time):
    frame = inputFrame
    if (current_frame % time == 0):
        frame += 1
    if (frame > maxFrames):
        frame = 0
    return frame
    
def Delay(inputFrame,frame,delay):
    if (inputFrame == (frame + delay)):
        return True
    else:
        return False


while True:

    if (playing):
        
        if (current_frame == 0):
            pygame.mixer.Sound.play(music,-1)
            waveStop = True
        #enemy spawn scalling
        if (current_frame == (60 * 60) * 0.05):
            pygame.mixer.Sound.play(hordeAlertList[random.randint(1,4)])
            waveStop = False
        if (current_frame == (60 * 60) * 0.5):
            waveStop = True
            pygame.mixer.Sound.play(breakAlert)
        if (current_frame == (60*60) * 0.8):
            waveStop = False
            pygame.mixer.Sound.play(hordeAlertList[random.randint(1,4)])
            bruteSpawnTime = 400
            ragerSpawnTime = 180
            bursterSpawnTime = 260
            enemySpawnTime = 30
            maxEnemies = 60
        
        if (WeaponSwapFrame == True):
            WeaponList = CheckWeapon(currentGun)
            damage = WeaponList[0]
            Total_Ammo = WeaponList[1]
            maxAmmo = WeaponList[1]
            magSize = WeaponList[2]
            ammo = WeaponList[2]
            Firerate = WeaponList[3]
            playerSpriteList = WeaponList[4]
            reloadTiming = WeaponList[5]
            shootSound = WeaponList[6]
            restockPrice = WeaponList[7]
            gunAudio = WeaponList[8]
            reloadSounds = WeaponList[9]
            ammo = magSize
            ammoSize = ammo
            WeaponSwapFrame = False

        #set int's to strings for printing
        coin_display = str(coin)
        Total_Ammo_display = str(Total_Ammo)
        ammo_display = str(ammo)
        playerHealthDis = str(playerHealth)
        resupPrice = str(restockPrice)
        # blit pictures
        screen.blit(background, (0, 0))  
        planeRect.x = 500
        planeRect.y = 600
        screen.blit(plane,(planeRect))
        #event loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and keys[pygame.K_w]:
            Current_Direction = Directions.UpAndLeft
        elif keys[pygame.K_d] and keys[pygame.K_w]:
            Current_Direction = Directions.UpAndRight
        elif keys[pygame.K_d] and keys[pygame.K_s]:
            Current_Direction = Directions.DownAndRight
        elif keys[pygame.K_a] and keys[pygame.K_s]:
            Current_Direction = Directions.DownAndLeft
        elif keys[pygame.K_a]:
            Current_Direction = Directions.Left
        elif keys[pygame.K_w]:
            Current_Direction = Directions.Up
        elif keys[pygame.K_d]:
            Current_Direction = Directions.Right
        elif keys[pygame.K_s]:
            Current_Direction = Directions.Down
        else:
            Current_Direction = Directions.InValid
        
        if keys[pygame.K_r]:
            R_pressed = True
        if keys[pygame.K_e]:
            E_pressed = True
        if not keys[pygame.K_e]:
            E_pressed = False
        if keys[pygame.K_n]:
            N_pressed = True
        if not keys[pygame.K_n]:
            N_pressed = False
        if keys[pygame.K_p]:
            P_pressed = True
        if not keys[pygame.K_p]:
            P_pressed = False
        if keys[pygame.K_t]:
            T_pressed = True
        if not keys[pygame.K_t]:
            T_pressed = False
        if keys[pygame.K_1]:
            pressed_1 = True
        if not keys[pygame.K_1]:
            pressed_1 = False
        if keys[pygame.K_3]:
            pressed_3 = True
        if not keys[pygame.K_3]:
            pressed_3 = False
        if keys[pygame.K_SPACE]:
            Space_pressed = True
        if not keys[pygame.K_SPACE]:
            Space_pressed = False
        
        mouse_buttons = pygame.mouse.get_pressed()
        M_pressed = mouse_buttons[0]  # Left mouse button
        
        # Player logic   
        mouse_x, mouse_y = pygame.mouse.get_pos()
        playerList = p1.MovePlayer(Current_Direction,Space_pressed,current_frame,dashCooldown)
        playerMoveX = (playerList[0] * MoveSpeed)
        playerMoveY = (playerList[1] * MoveSpeed)
        player_rect.x += playerMoveX
        player_rect.y += playerMoveY
        TrotX = mouse_x - player_rect.centerx 
        TrotY = mouse_y - player_rect.centery
        Tdist = math.hypot(TrotX, TrotY) + 0.000001  # prevents division by zero
        TdirX = (TrotX / Tdist) + 0.00000000001
        TdirY = (TrotY / Tdist) + 0.00000000001
        Tangle_radians = math.atan2(TrotY, TrotX)
        Tangle_degrees = math.degrees(Tangle_radians)
    
        # Player gun logic
        end_x = player_rect.x + TrotX * Tdist
        end_y = player_rect.y + TrotY * Tdist
        line_start = (player_rect.x + 50, player_rect.y + 50)
        line_end = end_x, end_y

        if (ammo <= 0) or (R_pressed == True):
            Is_reloading = True
            OutOfAmmo = True
            if (Frame_checker == reloadTiming[0]):
                pygame.mixer.Sound.play(reloadSounds[0])
                Frame_checker += 1
            elif (Frame_checker == reloadTiming[1]):
                pygame.mixer.Sound.play(reloadSounds[1])
                Frame_checker += 1
            elif (Frame_checker == reloadTiming[2]):
                pygame.mixer.Sound.play(reloadSounds[2])
                Frame_checker = 0
                Is_reloading = False
                if (Total_Ammo > magSize):
                    Total_Ammo -= magSize - ammo
                    ammo = magSize
                    Is_reloading = False
                elif (magSize >= ammo):
                    if (Total_Ammo - (magSize - ammo) < 0):
                        ammo = Total_Ammo
                        Total_Ammo = 0
                        Is_reloading = False
                    else:
                        Total_Ammo -= magSize - ammo
                        ammo = magSize
                        Is_reloading = False
                R_pressed = False
            else:
                Frame_checker += 1
        
        if (current_frame % Firerate) == 0 and (M_pressed) and (not Is_reloading) and (not OutOfAmmo):
            gun_firing_frame = True
            if (current_frame % Firerate) == 0:
                ammo -= 1
                if (current_frame % (Firerate * gunAudio) == 0):
                    if (ammo >= 1):
                        pygame.mixer.Sound.play(shootSound)
                gun_firing_frame = True
                frames_after_firing = 5

        if gun_firing_frame:
            if frames_after_firing > 0:
                current_player_frame = playerSpriteList[random.randint(1,3)]
                frames_after_firing -= 1
            else:
                current_player_frame = playerSpriteList[0]
                gun_firing_frame = False
        else:
            current_player_frame = playerSpriteList[0]
            gun_firing_frame = False

        rotated_player_image = pygame.transform.rotate(current_player_frame, -Tangle_degrees)
        playerRoatedRect = rotated_player_image.get_rect(center=player_rect.center)
        playerMask = pygame.mask.from_surface(rotated_player_image)
        placeHolderRect = player_rect
        placeHolderRect = pygame.Rect.scale_by(placeHolderRect,0.5)
        screen.blit(rotated_player_image, playerRoatedRect.topleft)

        #UI logic
        if (ammo == ammoSize):
            boxCoordX = 820
            boxCoordY = 615
            bullet_cube = pygame.transform.scale(bullet_cube, (50, 65))
        if (ammo <= (ammoSize * 0.8)):
            bullet_cube = pygame.transform.scale(bullet_cube, (50, (65 * 0.8)))
            boxCoordX = 820
            boxCoordY = 615 + (20 * 0.8)
        if (ammo <= (ammoSize * 0.6)):
            bullet_cube = pygame.transform.scale(bullet_cube, (50, (65 * 0.6)))
            boxCoordX = 820
            boxCoordY = 615 + (20 * 1.6)
        if (ammo <= (ammoSize * 0.4)):
            bullet_cube = pygame.transform.scale(bullet_cube, (50, (65 * 0.4)))
            boxCoordX = 820
            boxCoordY = 615 + (20 * 2.4)
        if (ammo <= (ammoSize * 0.2)):
            bullet_cube = pygame.transform.scale(bullet_cube, (50, (65 * 0.25)))
            boxCoordX = 820
            boxCoordY = 615 + (20 * 3)
        if (ammo == 0):
            bullet_cube = pygame.transform.scale(bullet_cube, (50, (65 * 0.25)))
            boxCoordX = 820
            boxCoordY = 700
            
        screen.blit(bullet_cube, (boxCoordX, boxCoordY))   
        screen.blit(terror_logo, (0, 0))
        screen.blit(bulletUI, (800, 600))
        screen.blit(white_line, (902.5,647.5))
        screen.blit(callInUI,(-51,542))

        #text
        gradient_text(screen, playerHealthDis, HL_font, (255, 0, 0), (0, 0, 0), (500, 500))
        gradient_text(screen, coin_display, HL_font, (255, 0, 0), (0, 0, 0), (45, 0))
        gradient_text(screen, ammo_display, HL_font, (255, 255, 255),(255, 255, 255),(902.5, 610))
        gradient_text(screen, Total_Ammo_display, HL_font, (255, 255, 255),(255, 255, 255),(902.5, 655))
        gradient_text(screen, resupPrice, HL_font, (255, 255, 255),(255, 255, 255),(22.5, 525))
        
        #shop logic
        if (pressed_1) and (coin >= restockPrice) and (not ammoRestock):
            ammoRect = ammo1.get_rect()
            ammoRect.x = playerRoatedRect.x + (random.randint(-100,100))
            if (ammoRect.x) >= 1000 or ammoRect.x < 0:
                ammoRect.x = playerRoatedRect.x
            ammoRect.y = playerRoatedRect.y + (random.randint(-50,50))
            if (ammoRect.y) >= 7000 or ammoRect.y < 0:
                ammoRect.y = playerRoatedRect.y
            coin -= restockPrice
            pressed_1 = False
            resupCallFrame = current_frame
            resupCalledIn = True

        if (resupCalledIn):
            resupFlareFrame = 0 + Animation(current_frame,3,resupFlareFrame,25)
            screen.blit(dropAnimationList[resupFlareFrame],ammoRect)
            
            if (Delay(current_frame,resupCallFrame,120)):
                pygame.mixer.Sound.play(supplyDropAlert)
                ammoRestock = True
                resupCalledIn = False

        if (ammoRestock):
            ammoFrame = 0 + Animation(current_frame,4,ammoFrame,10)
            screen.blit(ammoAnimationList[ammoFrame],ammoRect)
            if playerMask.overlap(ammoMask,(ammoRect.x - playerRoatedRect.x,ammoRect.y - playerRoatedRect.y)):
                Total_Ammo = maxAmmo
                ammoRestock = False

        if (pressed_3) and (coin >= medPackPrice) and (not medPackRestock):
            medPackRect = medPack1.get_rect()
            medPackRect.x = playerRoatedRect.x + (random.randint(-100,100))
            if (medPackRect.x) >= 1000 or medPackRect.x < 0:
                medPackRect.x = playerRoatedRect.x
            medPackRect.y = playerRoatedRect.y + (random.randint(-50,50))
            if (medPackRect.y) >= 7000 or medPackRect.y < 0:
                medPackRect.y = playerRoatedRect.y
            coin -= medPackPrice
            pressed_3 = False
            medPackCallFrame = current_frame
            medPackCalledIn = True

        if (medPackCalledIn):
            resupFlareFrame2 = 0 + Animation(current_frame,3,resupFlareFrame2,25)
            screen.blit(dropAnimationList[resupFlareFrame2],medPackRect)
            
            if (Delay(current_frame,medPackCallFrame,300)):
                medPackRestock = True
                medPackCalledIn = False

        if (medPackRestock):
            medPackAnimationFrame = 0 + Animation(current_frame,4,medPackAnimationFrame,15)
            screen.blit(medPackAnimationList[medPackAnimationFrame],medPackRect)
            if playerMask.overlap(medPackMask,(medPackRect.x - playerRoatedRect.x,medPackRect.y - playerRoatedRect.y)):
                playerHealth += 25
                if (playerHealth > 50):
                    playerHealth = 50
                medPackRestock = False
            
        if pygame.Rect.colliderect(planeRect,player_rect) and (E_pressed == True):
            if (coin >= 500):
                coin -= 500
                currentGun = "MK2ravager"
                WeaponSwapFrame = True
                E_pressed = False
                Is_reloading = False
            else:
                E_pressed = False

        if pygame.Rect.colliderect(planeRect,player_rect) and (N_pressed):
            if (coin >= 750):
                coin -= 750
                currentGun = "SMG"
                WeaponSwapFrame = True
                N_pressed = False
                Is_reloading = False
            else:
                N_pressed = False

        if pygame.Rect.colliderect(planeRect,player_rect) and (T_pressed):
            if (coin >= 100):
                coin -= 100
                currentGun = "MK1ravager"
                WeaponSwapFrame = True
                N_pressed = False
                Is_reloading = False
            else:
                T_pressed = False

        bursterIndex = []

        #burster logic
        if (not waveStop):
            if (current_frame % bursterSpawnTime == 0):
                burster_x = random.randint(0, 1000)
                bursterXList.append(burster_x)
                bursterYList.append(0)
                bursterHealthList.append(bursterHealth)

        for x in range(len(bursterXList)):
            bursterCoords = [bursterXList[x], bursterYList[x]]
            bursterRotData = GetRotationAngle(placeHolderRect, bursterCoords)
            bursterXList[x] = MoveEnemyX(bursterRotData[0], bursterRotData[1], bursterXList[x], bursterSpeed)
            bursterYList[x] = MoveEnemyY(bursterRotData[0], bursterRotData[1], bursterYList[x], bursterSpeed)
            bursterRoated = pygame.transform.rotate(bursterAnimationList[frame_offset], -bursterRotData[2])
            bursterRect = bursterRoated.get_rect(center=(bursterXList[x], bursterYList[x]))

            if bursterRect.clipline(line_start, line_end):
                bursterClippedLine = True
            else:
                bursterClippedLine = False

            if not OutOfAmmo:
                if g1.FireGun(M_pressed, Firerate, current_frame, bursterClippedLine, Gun_already_fired, Is_reloading):
                    bursterHealthList[x] -= damage

            if bursterHealthList[x] <= 0:
                bursterIndex.append(x)
                coin += 10
                pygame.mixer.Sound.play(ragerDeath)
            
            screen.blit(bursterRoated, bursterRect.topleft)

        for index in sorted(bursterIndex, reverse=True):
            del bursterXList[index]
            del bursterYList[index]
            del bursterHealthList[index]

        #rager logic
        if (not waveStop):
            if (current_frame % ragerSpawnTime == 0):
                ragerX = random.randint(0, 1000)
                ragerXList.append(ragerX)
                ragerYList.append(0)
                ragerHealthList.append(ragerHealth)

        ragerIndex = []

        for x in range(len(ragerXList)):
            ragerCoords = [ragerXList[x], ragerYList[x]]
            ragerRotData = GetRotationAngle(placeHolderRect, ragerCoords)
            ragerXList[x] = MoveEnemyX(ragerRotData[0], ragerRotData[1], ragerXList[x], ragerSpeed)
            ragerYList[x] = MoveEnemyY(ragerRotData[0], ragerRotData[1], ragerYList[x], ragerSpeed)
            ragerRoated = pygame.transform.rotate(ragerAnimationList[frame_offset], -ragerRotData[2])
            ragerMask = pygame.mask.from_surface(ragerRoated)
            ragerRect = ragerRoated.get_rect(center=(ragerXList[x], ragerYList[x]))
            ragerPlaceholderRect = pygame.Rect.scale_by(ragerRect,2)


            if ragerRect.clipline(line_start, line_end):
                ragerClippedLine = True
            else:
                ragerClippedLine = False

            if not OutOfAmmo:
                if g1.FireGun(M_pressed, Firerate, current_frame, ragerClippedLine, Gun_already_fired, Is_reloading):
                    ragerHealthList[x] -= damage

            if ragerHealthList[x] <= 0:
                ragerIndex.append(x)
                coin += 10
                pygame.mixer.Sound.play(ragerDeath)  

            if playerMask.overlap(ragerMask,(ragerRect.x - playerRoatedRect.x,ragerRect.y - playerRoatedRect.y)):
                ragerHitPlayer = True
            
            screen.blit(ragerRoated, ragerRect.topleft)  
        
        if (ragerHitPlayer):
            if (ragerHitCooldown == 0):
                playerHealth -=  ragerDamage
                ragerHitTimer = True
        if (ragerHitPlayer and ragerHitCooldown < ragerCooldown):
            ragerHitCooldown += 1
        if (ragerHitCooldown == ragerCooldown):
            ragerHitTimer = False
            ragerHitCooldown = 0
            ragerHitPlayer = False

        for index in sorted(ragerIndex, reverse=True): #idk how this works but ok
            del ragerXList[index]
            del ragerYList[index]
            del ragerHealthList[index]  
        
        
        # Enemy logic
        enemyIndex = []
        if (not waveStop):
            if current_frame % enemySpawnTime == 0:
                if len(enemy_Xlist) <= maxEnemies:
                    enemy_x = random.randint(0, 1000)
                    enemy_Xlist.append(enemy_x)
                    enemy_Ylist.append(0)
                    enemyHealthList.append(enemyHealth)

        for x in range(len(enemy_Xlist)):
            enemy_coords = [enemy_Xlist[x], enemy_Ylist[x]]
            enemyRotData = GetRotationAngle(placeHolderRect, enemy_coords)
            enemy_Xlist[x] = MoveEnemyX(enemyRotData[0], enemyRotData[1], enemy_Xlist[x],enemy_speed) 
            enemy_Ylist[x] = MoveEnemyY(enemyRotData[0], enemyRotData[1], enemy_Ylist[x],enemy_speed)
            if current_frame % 10 == 0:
                frame_offset = random.randint(0, 1)
            rotated_enemy = pygame.transform.rotate(chainsaw_animation_list[frame_offset], -enemyRotData[2])
            rotated_rect = rotated_enemy.get_rect(center=(enemy_Xlist[x],enemy_Ylist[x]))
            enemyMask = pygame.mask.from_surface(rotated_enemy)
            
            if rotated_rect.clipline(line_start, line_end):
                Enemy_Clipped_line = True
            else:
                Enemy_Clipped_line = False
            
            if (OutOfAmmo == False):
                if g1.FireGun(M_pressed,Firerate,current_frame,Enemy_Clipped_line,Gun_already_fired,Is_reloading):
                    enemyHealthList[x] -= damage
            
            if (enemyHealthList[x] <= 0):
                coin += 1    
                enemyIndex.append(x)      
                if (random.randint(1,3)) == 2:
                    pygame.mixer.Sound.play(enemy_death)  
            
            if playerMask.overlap(enemyMask,(rotated_rect.x - playerRoatedRect.x,rotated_rect.y - playerRoatedRect.y)):
                enemyHitPlayer = True
            
            screen.blit(rotated_enemy, rotated_rect.topleft)

        if (enemyHitPlayer):
            if (enemyHitCooldown == 0):
                playerHealth -=  enemyDamage
                enemyHitTimer = True
        if (enemyHitTimer and enemyHitCooldown < enemyCooldown):
            enemyHitCooldown += 1
        if (enemyHitCooldown == enemyCooldown):
            enemyHitTimer = False
            enemyHitCooldown = 0
            enemyHitPlayer = False

        for index in sorted(enemyIndex, reverse=True):
            del enemy_Xlist[index]
            del enemy_Ylist[index]
            del enemyHealthList[index]
        

        #brute logic
        if (not waveStop):
            if (current_frame % bruteSpawnTime == 0):
                brute_x = random.randint(0, 1000)
                bruteXList.append(brute_x)
                bruteYList.append(0)
                bruteHealthList.append(bruteHealth)
                bruteSpeedList.append(1)

        bruteIndex = []

        for x in range(len(bruteXList)):
            resultSpeed = (bruteSpeed * bruteSpeedList[x])
            bruteCoords = [bruteXList[x], bruteYList[x]]
            bruteRotData = GetRotationAngle(placeHolderRect, bruteCoords)
            bruteXList[x] = MoveEnemyX(bruteRotData[0], bruteRotData[1], bruteXList[x], resultSpeed)
            bruteYList[x] = MoveEnemyY(bruteRotData[0], bruteRotData[1], bruteYList[x], resultSpeed)
            bruteRoated = pygame.transform.rotate(bruteAnimationList[frame_offset], -bruteRotData[2])
            bruteMask = pygame.mask.from_surface(bruteRoated)
            bruteRect = bruteRoated.get_rect(center=(bruteXList[x], bruteYList[x]))
            distFromPlayer = math.hypot(bruteRotData[0], bruteRotData[1])
            distFromPlayer = (distFromPlayer / 25)
            if (distFromPlayer <= 6):
                bruteSpeedList[x] = 2.5
            if (distFromPlayer > 6):
                bruteSpeedList[x] = 1

            if bruteRect.clipline(line_start, line_end):
                bruteClippedLine = True
            else:
                bruteClippedLine = False

            if not OutOfAmmo:
                if g1.FireGun(M_pressed, Firerate, current_frame, bruteClippedLine, Gun_already_fired, Is_reloading):
                    bruteHealthList[x] -= damage

            if bruteHealthList[x] <= 0:
                bruteIndex.append(x)
                coin += 10
                pygame.mixer.Sound.play(bruteDeath) 

            if playerMask.overlap(bruteMask,(bruteRect.x - playerRoatedRect.x,bruteRect.y - playerRoatedRect.y)):
                bruteHitPlayer = True
            
            screen.blit(bruteRoated, bruteRect.topleft)
        
        if (bruteHitPlayer):
            if (bruteHitCooldown == 0):  
                playerHealth -=  bruteDamage
                bruteHitTimer = True
        if (bruteHitTimer and bruteHitCooldown < bruteCooldown):
            bruteHitCooldown += 1
        if (bruteHitCooldown == bruteCooldown):
            bruteHitTimer = False
            bruteHitCooldown = 0
            bruteHitPlayer = False

        for index in sorted(bruteIndex, reverse=True): #idk how this works but ok
            del bruteXList[index]
            del bruteYList[index]
            del bruteHealthList[index]
            del bruteSpeedList[index]

        #reset bools
        Gun_already_fired = False
        OutOfAmmo = False

        #increment frame
        current_frame += 1
        #display
        coin_display = str(coin)
        
        if (playerHealth <= 0):
            R_pressed = False
            M_pressed = False
            Space_pressed = False
            E_pressed = False
            N_pressed = False
            P_pressed = False
            T_pressed = False
            pressed_1 = False
            pressed_3 = False
            ESC_pressed = False
            current_frame = 1
            frame_offset = 0
            Frame_checker = 0
            player_frame_offest = 0
            WeaponSwapFrame = False
            ammoFrame = 0
            ammoFrame2 = 0
            resupFlareFrame = 0
            resupFlareFrame2 = 0
            medPackAnimationFrame = 0
            lastFrameNotFired = 0
            eliteEnemyTime = 180
            enemySpawnTime = 10
            maxEnemies = 100
            coin = 1
            restockPrice = 75
            resupCallFrame = 0
            resupCalledIn = False
            medPackCallFrame = 0
            medPackCalledIn = False
            medPackPrice = 10
            medPackRestock = False
            shopTest = False
            resupBlit = False
            ammoShopBuy = False
            ammoRestock = False
            player_rect.x = 400
            player_rect.y = 250
            MoveSpeed = 1.2
            dashCooldown = 45
            playerHealth = 50
            current_player_frame = player_frame_1
            enemy_speed = 1.4
            enemyHealth = 5
            enemyDamage = 3
            enemyHitCooldown = 0
            enemyCooldown = 90
            enemyHitTimer = False
            enemy_Xlist = []
            enemy_Ylist = []
            enemyHealthList = []
            CanSpawnEnemy = True
            enemyHitPlayer = False
            bruteHitCooldown = 0
            bruteHitPlayer = False
            bruteHitTimer = False
            bruteHealthList = []
            bruteXList = []
            bruteYList = []
            bruteChargeSpeedList = []
            bruteChargeTiming = []
            bruteChargeRot = []
            bruteChargingList = []
            ragerHitCooldown = 0
            ragerHitPlayer = False
            ragerHealthList = []
            ragerXList = []
            ragerYList = []
            bursterHealthList = []
            bursterXList = []
            bursterYList = []
            Gun_already_fired = False
            Is_reloading = False
            WeaponSwapFrame = True
            currentGun = "flex"
            reloadList = [gun_Open, gun_Reload, gun_Close]
            gun_firing_frame = False
            CanShoot = False
            OutOfAmmo = False
            currentEnemyWave = 1

    if (mainMenu):
        screen.blit(background,(0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            mouse_buttons = pygame.mouse.get_pressed()
            keys = pygame.key.get_pressed()
            Lmouse = mouse_buttons[0]
            Rmouse = mouse_buttons[1]
     
        mousePos = pygame.mouse.get_pos()
        
        if MenuFrame % 45 == 0:
            if len(menuEnemy_Xlist) <= 25:
                menuEnemy_x = random.randint(0, 1000)
                menuEnemy_Xlist.append(menuEnemy_x)
                menuEnemy_Ylist.append(-25)
        for x in range(len(menuEnemy_Xlist)):
            menuEnemy_Ylist[x] += 1
            if MenuFrame % 10 == 0:
                menuFrame_offset = random.randint(0, 1)
            if (menuEnemy_Ylist[x] >= 700):
                menuEnemy_Ylist[x] = 0
            screen.blit(menuEnemySprites[menuFrame_offset],(menuEnemy_Xlist[x],menuEnemy_Ylist[x]))

        if MenuFrame % 280 == 0:
            if len(menuBrute_Xlist) <= 25:
                menuBrute_x = random.randint(0, 1000)
                menuBrute_Xlist.append(menuBrute_x)
                menuBrute_Ylist.append(-25)
        for x in range(len(menuBrute_Xlist)):
            menuBrute_Ylist[x] += 0.5
            if MenuFrame % 10 == 0:
                menuFrame_offset = random.randint(0, 1)
            if (menuBrute_Ylist[x] >= 700):
                menuBrute_Ylist[x] = 0
                menuBrute_Xlist[x] = random.randint(0, 1000)
            screen.blit(menuBruteSprites[menuFrame_offset],(menuBrute_Xlist[x],menuBrute_Ylist[x]))

        if (MenuFrame + 120) % 280 == 0:
            if len(menuRager_Xlist) <= 25:
                menuRager_x = random.randint(0, 1000)
                menuRager_Xlist.append(menuRager_x)
                menuRager_Ylist.append(-25)
        for x in range(len(menuRager_Xlist)):
            menuRager_Ylist[x] += 2
            if MenuFrame % 10 == 0:
                menuFrame_offset = random.randint(0, 1)
            if (menuRager_Ylist[x] >= 700):
                menuRager_Ylist[x] = 0
                menuRager_Xlist[x] = random.randint(0, 1000)
            screen.blit(menuRagerSprites[menuFrame_offset],(menuRager_Xlist[x],menuRager_Ylist[x]))

        MenuFrame += 1

        if Lmouse and playButtonRect.collidepoint(mousePos):
            mainMenu = False
            playing = True
            guideMenu = False
        
        if Lmouse and guideButtonRect.collidepoint(mousePos):
            mainMenu = False
            Playing = False
            guideMenu = True

        screen.blit(gameLogo,(0,15))

    if (guideMenu):
        screen.blit(background,(0,0))
        screen.blit(guide1,(0,0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            mouse_buttons = pygame.mouse.get_pressed()
            keys = pygame.key.get_pressed()
            Lmouse = mouse_buttons[0]
            Rmouse = mouse_buttons[1]

            if keys[pygame.K_ESCAPE]:
                    ESC_pressed = True
            if not keys[pygame.K_ESCAPE]:
                ESC_pressed = False
        if (ESC_pressed):
            mainMenu = True
            Playing = False
            guideMenu = False

    pygame.display.update()
    clock.tick(60)
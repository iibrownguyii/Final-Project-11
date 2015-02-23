# classes.py

from pygame import *
from random import *
from math import *
from enum import *

class player:
    def __init__(self, name, health, house, level, spell_level, potion_level, stamina, speed, x, y, moveMode):
        self.name = name
        self.health = health
        self.house = house
        self.level = level
        self.spell_level = spell_level
        self.potion_level = potion_level
        self.stamina = stamina
        self.speed = speed
        self.x = x
        self.y = y
        self.moveMode = moveMode
        self.playerRect = Rect(x, y, 40, 50)
        self.width = self.playerRect[2]
        self.height = self. playerRect[3]

    def move(self, pressed, screen):
        "Move player"
        if self.moveMode == "wasd":  # temporary use enumerations
            if pressed[K_w]:
                self.y -= self.speed
            if pressed[K_s]:
                self.y += self.speed
            if pressed[K_a]:
                self.x -= self.speed
            if pressed[K_d]:
                self.x += self.speed

        if self.moveMode == "arrow":
            if pressed[K_UP]:
                self.y -= self.speed
            if pressed[K_DOWN]:
                self.y += self.speed
            if pressed[K_LEFT]:
                self.x -= self.speed
            if pressed[K_RIGHT]:
                self.x += self.speed

        self.playerRect = Rect(self.x, self.y, 40, 50)
        draw.rect(screen, (0, 255, 0), self.playerRect)


    # get meathods
    def getSpeed(self):
        "get speed of object"
        return self.speed
    
    def getX(self):
        "get x position of object"
        return self.x
    
    def getY(self):
        "get y position of object"
        return self.y
    
    def getWidth(self):
        "get width of player"
        return self.width
    
    def getHeight(self):
        "get length of player"
        return self.height
    
    def getRect(self):
        "get the rect of object"
        return self.playerRect
    
    def getHealth(self):
        "get health of player"
        return self.health
    
    def gotHit(self):
        "do things for being hit"
        self.health -= 1

class enemy:
    def __init__(self, health, speed, AI_level, attack_radius, kind, x, y):
        self.x = x
        self.y = y
        self.health = health
        self.follow_radius = attack_radius + randint(50,150)
        self.attack_radius = attack_radius
        self.enemyRect = Rect(x, y, 40, 50)
        self.speed = speed
        self.AI_level = AI_level
        self.kind = kind

    def move(self, px, py, screen):
        "Move enemy"
        #draw.circle(screen, (0, 0, 148, 30), (int(self.x)+20, int(self.y)+25), self.follow_radius)
        #draw.circle(screen, (148, 0, 0, 30), (int(self.x)+20, int(self.y)+25), self.attack_radius)
        if sqrt((px-self.x)**2 + (py - self.y)**2) < self.follow_radius:
            if py > self.y:
                self.y += self.speed
            if py < self.y:
                self.y -= self.speed
            if px > self.x:
                self.x += self.speed
            if px < self.x:
                self.x -= self.speed

        self.enemyRect = Rect(self.x, self.y, 40, 50)
        draw.rect(screen, (255, 0, 0), self.enemyRect)

    def AI(self):
        "AI for enemies"

    def checkCollision(self, rleft, rtop, width, height, center_x, center_y, radius):
        "Detect collision between a rectangle and circle"

        # complete boundbox of the rectangle
        rright, rbottom = rleft + width/2, rtop + height/2

        # bounding box of the circle
        cleft, ctop     = center_x-radius, center_y-radius
        cright, cbottom = center_x+radius, center_y+radius

        # trivial reject if bounding boxes do not intersect
        if rright < cleft or rleft > cright or rbottom < ctop or rtop > cbottom:
            return False  # no collision possible

        # check whether any point of rectangle is inside circle's radius
        for x in (rleft, rleft+width):
            for y in (rtop, rtop+height):
                # compare distance between circle's center point and each point of
                # the rectangle with the circle's radius
                if hypot(x-center_x, y-center_y) <= radius:
                    return True  # collision detected

        # check if center of circle is inside rectangle
        if rleft <= center_x <= rright and rtop <= center_y <= rbottom:
            return True  # overlaid

        return False  # no collision detected


    # get methods
    def getX(self):
        "get x position of object"
        return self.x

    def getY(self):
        "get y position of object"
        return self.y

    def getAttackRadius(self):
        "get the attack radius"
        return self.attack_radius

    def getHealth(self):
    	"get health of enemy"
    	return self.health

    # fix
    def getVector(self, px, py):
        "get direction vector of enemy"
        if self.x <= px and self.y >= py:
            ang = degrees(atan2(radians(self.speed),radians(self.speed)))
            mag = sqrt(2*(self.speed**2))
        elif self.x <= px and self.y <= py:
            ang = degrees(atan2(radians(self.speed),radians(-self.speed)))
            mag = sqrt(2*(self.speed**2))
        elif self.x >= px and self.y <= py:
            ang = degrees(atan2(radians(-self.speed),radians(-self.speed)))
            mag = sqrt(2*(self.speed**2))
        elif self.x >= px and self.y >= py:
            ang = degrees(atan2(radians(-self.speed),radians(self.speed)))
            mag = sqrt(2*(self.speed**2))
        elif self.x <= px and self.y == py:
            ang = 0
            mag = self.speed
        elif self.x >= px and self.y == py:
            ang = 180
            mag = self.speed
        elif self.y <= py and self.x == px:
            ang = 270
            mag = self.speed
        elif self.y >= py and self.x == px:
            ang = 90
            mag = self.speed
        return(ang,mag)

# enumeration
class playerMode(Enum):
    player_1 = 1
    player_2 = 2

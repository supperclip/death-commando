from enum import Enum
import pygame
import sys
from pygame.locals import QUIT

class Directions(Enum):
    InValid = 0
    Up = 1
    Down = 2
    Right = 3
    Left = 4
    UpAndRight = 5
    UpAndLeft = 6
    DownAndRight = 7
    DownAndLeft = 8

class player:
    def __init__(self,PlayerDirection,space,tick,dashCooldown):
        self.PlayerDirection = PlayerDirection
        self.space = space
        self.last_tick = tick
        self.dashCooldown = dashCooldown
    
    def MovePlayer(self, PlayerDirection,space,tick,dashCooldown):
        now = tick
        dash = False
        dashSpeed = 1
        if (space):
            if (now - self.last_tick) >= dashCooldown:
                self.last_tick = now
                dash = True
                dashCall = tick
                if (dash):
                    dashSpeed = 15 - (0.5* (now - self.last_tick))
                if (dashCall == (now + 30)):
                    dash = False
        
        if PlayerDirection == Directions.InValid:
            return [0 * dashSpeed,0 * dashSpeed]
        if PlayerDirection == Directions.UpAndLeft:
            return [-1 * dashSpeed,-1 * dashSpeed]
        if PlayerDirection == Directions.UpAndRight:
            return [1 * dashSpeed,-1 * dashSpeed]
        if PlayerDirection == Directions.DownAndLeft:
            return [-1 * dashSpeed,1 * dashSpeed]
        if PlayerDirection == Directions.DownAndRight:
            return [1 * dashSpeed,1 * dashSpeed]
        elif PlayerDirection == Directions.Right:
            return [1 * dashSpeed,0 * dashSpeed]
        elif PlayerDirection == Directions.Left:
            return [-1 * dashSpeed,0 * dashSpeed]
        elif PlayerDirection == Directions.Up:
            return [0 * dashSpeed,-1 * dashSpeed]
        elif PlayerDirection == Directions.Down:
            return [0 * dashSpeed,1 * dashSpeed]
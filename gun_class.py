class GunLogic:
    def __init__(self, MousePressed, Firerate, Tick,enemyHit,GunFired,Reloading):
        self.MousePressed = MousePressed
        self.Firerate = Firerate
        self.last_tick = Tick  # Store the last tick time
        self.enemyHit = enemyHit
        self.GunFired = GunFired
        self.Reloading = Reloading

    def FireGun(self, MousePressed, Firerate, tick,enemyHit,GunFired,Reloading):
        now = tick  # Always define `now` with the current tick
        if GunFired == False:
            if (MousePressed == True and enemyHit == True and Reloading == False):
                if (now - self.last_tick) >= Firerate:
                    self.last_tick = now
                    return True
                else:
                    return False 
            else:
                return False
        else:
            return False
            
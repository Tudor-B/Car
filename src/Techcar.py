

class car(object):
    speed = 0
    position = 0
    accel = 0
    maxspeed = 100
    alloweddistance = 150
    normaldistance = 250
    maxdistance= 350
    nextCar = None
    def __init__(self,speed=0, position=0,maxspeed=100):
        self.speed = speed
        self.position = position
        self.maxspeed = maxspeed

    
    def getSpeed(self):
        return self.speed
    
    def getAccel(self):
        return self.accel
    
    def getPosition(self):
        return self.position
    
    def getMaxSpeed(self):
        return self.maxspeed
    
    def getDistanceForward(self, othercar):
        if othercar == None:
            return 999
        else:
            distance = othercar.getPosition() - self.getPosition()
            return distance
    
    def getDistanceBehind(self, othercar):
        distance = self.getPosition() - othercar.getPosition()
        return distance
    
    
    def setSpeed(self, speed):
        if speed != 0:
            self.speed = speed
        else:
            self.speed = self.getSpeed() + self.getAccel()
    
    def setAccel(self, accel):
        self.accel = accel
        
    
    def doDrive(self):
        self.speed=self.getSpeed() + self.getAccel()
        self.position = self.getPosition() + self.getSpeed()
        
    def doAccel(self):
        self.speed = self.speed + self.accel

    
if __name__ == "__main__":
    pass
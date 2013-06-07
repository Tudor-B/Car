
from Techcar import car
parameters = {}
i=1
try:
    firstcar=car()
    f = open('Input.txt')
    parameters = {}
    for line in f:
        line = line.split('=')
        parameters[line[0]] = int(line[1])
        
#     print parameters
    
    
    secondcar=car()
    

    firstcar.setAccel(parameters['firstAccel'])
    secondcar.position=parameters['secondPos']
    secondcar.speed=parameters['secondSpeed']
    
    print "Car has started moving"

    while firstcar.getPosition()<4000:
        firstcar.doDrive()
        print "At measure", i, " the automated car was situated at" ,firstcar.getPosition()
        print "At measure", i, " the autmated car had the speed of" , firstcar.getSpeed()
        print "At measure", i, " the automated car had the acceleration of", firstcar.getAccel()
        secondcar.doDrive()
        print "At measure", i, " the normal car was situated at", secondcar.getPosition()
        print "At measure", i, " the normal car had the speed of", secondcar.getSpeed()
        print "At measure", i, " the normal car had the acceleration of", secondcar.getAccel()
        
        if firstcar.getDistanceForward(secondcar) < firstcar.normaldistance:
            firstcar.accel=-10
            print "Reducing speed with", -firstcar.getAccel()
            if firstcar.getSpeed()<secondcar.getSpeed():
                firstcar.accel=5
                print "Accelerating with", firstcar.getAccel()
        elif firstcar.getDistanceForward(secondcar) < firstcar.alloweddistance:
            firstcar.accel=-30
            print "Urgent braking"
        
        if firstcar.getDistanceForward(secondcar) > firstcar.normaldistance:
            firstcar.accel=10
            print "Accelerating with", firstcar.getAccel()
        print "-------------Next Measure------------"
        i=i+1
#             firstcar.accel=firstcar.accel
#         elif firstcar.getDistanceForward(secondcar) > firstcar.maxdistance:
#             firstcar.accel=firstcar.accel+5
    


except Exception, e:
    print "Unhandled exception: %s"%e
    print "Shutting down now"
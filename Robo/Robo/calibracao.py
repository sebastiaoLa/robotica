from ev3dev.ev3 import *

biggerRed = 0
smallerRed = 255
biggerGreen = 0
smallerGreen = 255
biggerBlue = 0
smallerBlue = 255

colorE = ColorSensor('in1')

for i in range(3000):
    raw = colorE.raw

    if biggerRed<raw[0]:
        biggerRed = raw[0]
    if smallerRed>raw[0]:
        smallerRed = raw[0]
    if biggerGreen<raw[1]:
        biggerGreen = raw[1]
    if smallerGreen>raw[1]:
        smallerGreen = raw[1]
    if biggerBlue<raw[2]:
        biggerBlue = raw[2]
    if smallerBlue >raw[2]:
        smallerBlue = raw[2]
    print (raw)


print ("Red:",biggerRed,smallerRed)    
print ("Green:",biggerGreen,smallerGreen)
print ("Blue:", biggerBlue,smallerBlue)


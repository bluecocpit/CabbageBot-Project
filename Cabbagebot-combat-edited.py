import time
import random

global ogrehp
ogrehp = 10
#ogrehp is Ogre's HP
    
global ogreap
ogreap = 3
#ogreat is Ogre's attack point (AP)

global magehp
magehp = 7

global mageap
mageap = 5


    
global mypethp
mypethp = 20
#mypethp is MyPet's HP
    
global mypetap 
mypetap = 4
#mypetap is MyPet's AP (Attack Point)

global attackedtime
attackedtime = 1

global truedamageogre
truedamageogre = mypetap * attackedtime

global truedamagemypet
truedamagemypet = ogreap * attackedtime

while ogrehp > 0 and mypethp > 0:
    print("Martin hit","monster",'!')
    time.sleep(0.75)
    ogrehp = ogrehp - mypetap
    print("Current Ogre's HP:",ogrehp)
    time.sleep(0.75)
    print("monster hit Martin!")
    time.sleep(0.75)
    mypethp = mypethp - ogreap
    print("Current Mypet's HP:",mypethp)
    time.sleep(0.75)
    if ogrehp < 0:
        print("You bet","monster","!")
    if mypethp < 0:
        print("You lose!")

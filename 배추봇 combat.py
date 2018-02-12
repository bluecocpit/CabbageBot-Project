import random
import time


def combat():
    #combat 함수는 2018년 02월 11일에 완성됨 with 아빠.
    enemylist = ["Ogre","Mage"]
    
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

    


    enemy = random.choice(enemylist)
    print("You met", enemy,"!")
    time.sleep(1)
    if enemy == "Ogre":
         print(enemy,"'s hp is",ogrehp,'.')
         time.sleep(0.5)
         print(enemy,"'s ap is",ogreap,'.')
    else:
        print(enemy,"'s hp is",magehp,'.')
        time.sleep(0.5)
        print(enemy,"'s ap is",mageap,'.')

    while ogrehp-truedamagemypet > 0 and mypethp-truedamageogre > 0:
            print("Martin hit",enemy,'!')
            time.sleep(0.75)
            ogrehp = ogrehp-truedamagemypet
            print("Current Ogre's HP:",ogrehp)
            time.sleep(0.75)
            print(enemy,"hit Martin!")
            time.sleep(0.75)
            mypethp = mypethp-truedamageogre
            print("Current Mypet's HP:",mypethp)
            time.sleep(0.75)
            if ogrehp < 1:
                print("You bet",enemy,"!")
            if mypethp < 1:
                print("You lose!")
            
    #else:
    #    print("Whattttttttttttttttttttttt?????????????????????")
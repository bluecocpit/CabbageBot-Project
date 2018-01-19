import random
import time




#print("Hello? I am Cabbagebot.")
#time.sleep(1)
#name = input("What is your name?")
#print("Hello,", name)



def combat():
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
    mypetap = 2
    #mypetap is MyPet's AP (Attack Point)

    global attackedtime
    attackedtime = 0


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

    while ogrehp > 1 or mypethp > 1:

        while attackedtime in range(99999):
            truedamageogre = mypetap * attackedtime
            truedamagemypet = ogreap * attackedtime
            print("Martin hit",enemy,'!')
            time.sleep(0.75)
            print("Current Ogre's HP:",ogrehp-truedamagemypet)
            time.sleep(0.75)
            print(enemy,"hit Martin!")
            time.sleep(0.75)
            print("Current Mypet's HP:",mypethp-truedamageogre)
            time.sleep(0.75)
            if ogrehp < 1:
                print("You bet",enemy,"!")
            if mypethp < 1:
                print("You lose!")
            

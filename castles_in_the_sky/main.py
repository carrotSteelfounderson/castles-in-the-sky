import random
import time as t
import battle_sim as f
import sys as s
import gunnarSkale as GSK
alleigance = 'neutral'
credit = 0
fuel = 20
blackMarketEntryCode = None
missionMap = ['anacreon',
              'terminus',
              'trantor',
              'smyrno',
              'loris',
              'kalgan']
mapOne = {'anacreon':['terminus', 'trantor', 'smyrno', 'loris'],
          'terminus':['anacreon', 'zoranel 1', 'smyrno', 'loris'],
          'trantor':['anacreon', 'smyrno', 'kalgan', 'tazenda'],
          'zoranel 1':['zoranel 2', 'zoranel 3'],
          'zoranel 2':['zoranel 1', 'zoranel 3', 'zoranel 4'],
          'zoranel 3':['zoranel 1', 'zoranel 2', 'zoranel 4', 'zoranel 5'],
          'zoranel 4':['zoranel 5'], 'zoranel 5':['zoranel 1', 'sagitarius'],
          'smyrno':['terminus', 'anacreon', 'trantor', 'loris'],
          'loris':['smyrno', 'terminus', 'anacreon', 'kalgan'],
          'kalgan':['trantor', 'loris'],
          'tazenda':['trantor']}
mapTwo = {'anacreon':['station("anacreon")', 'gPlanet()', 'fightZone("l", "anacreon")'],
          'terminus':['fightZone("i", "terminus")', 'station("terminus")', 'rPlanet("terminus")'],
          'trantor':['fightZone("h", "trantor")', 'rPlanet("trantor")', 'station("trantor")'],
          'kalgan':['station("kalgan")', 'rPlanet("kalgan")', 'station("kalgan")', ],
          'smyrno':['fightZone("l", "smyrno")', 'gPlanet()', 'station("smyrno")'],
          'zoranel 1': ['gPlanet()'],
          'zoranel 2': ['gPlanet()'],
          'zoranel 3': ['gPlanet()'],
          'zoranel 4': ['gPlanet()'],
          'zoranel 5': ['gPlanet()'],
          'loris': ['fightZone("l", "loris")', 'station("loris")', 'gPlanet()'],
          'tazenda': ['rPlanet("tazenda")', 'fightZone("i", "tazenda")', 'rPlanet("tazenda")', 'fightZone("h", "tazenda")', 'rPlanet("tazenda")', 'gS("tazenda")']}
mapThree = {'anacreon': 3,
            'terminus': 7,
            'trantor': -6,
            'zoranel 1': 0,
            'zoranel 2': 0,
            'kalgan': -5,
            'tazenda': -1,
            'loris': -2,
            'smyrno': 3}
prices = {'motion tracking': 5,
          'electro-pulse': 6,
          'chaff': 2,
          'beam lensing': 3,
          'rapid fire': 7,
          'magnetic disintegrator': 4}
descriptions = {'motion tracking': 'prevents missing, by tracking the enemy',
                'electro-pulse': 'sends out a pulse disabling all missiles',
                'chaff': 'blasts debris interfering with radar and tracking',
                'beam lensing': 'focuses lasers meaning they cause more damage',
                'rapid fire': 'gives you an extra go',
                'magnetic disintegrator': 'uses magnetism to cause the enemy\'s hull to break up'}
mission = {'target': '',
           'cargo': '',
           'reward': 0}
bounty = {'foundation': 0,
          'empire': 0,
          'general': 0}
blackCommodities = {'gold': 5,
                    'Narcotics': 4,
                    'spirits': 1,
                    'computer chips': 3}
upgrades = ['motion tracking',
            'electro-pulse',
            'chaff',
            'beam lensing',
            'rapid fire',
            'magnetic disintegrator']
missionCargoes = ['motion tracking',
                  'electro-pulse',
                  'chaff',
                  'beam lensing',
                  'rapid fire',
                  'magnetic disintegrator',
                  'info',
                  'info',
                  'info',
                  'info',
                  'info',
                  'info',
                  'info',
                  'info']
def fightZone(level, system):
    global credit
    global alleigance
    s = False
    if level == 'l':
        print('you are in a low combat zone')
        if random.randint(1, 5) == 1:
            f.main()
            s = True
    if level == 'i':
        print('you are in an intermediate combat zone')
        if random.randint(1, 2) == 1:
            f.main()
            s = True
    if level == 'h':
        print('you are in a high combat zone')
        f.main()
        credit += random.randrange(1, 2, 4)
        s = True
    if level == 'n':
        print('you have been attacked by a bounty hunter')
        f.main()
        s = True
        return None
    if level == 'y':
        print('you have attacked a combat ship')
        f.main()
        s = True
    if s == False and input('do you want to fight: y/n') == 'y':
        f.main()
        credit += random.randrange(1, 2, 4)
    else:
        if alleigance == 'empire':
            mapThree[system] -= 1
        elif alleigance == 'foundation':
            mapThree[system] += 1
def station(system):
    global credit
    global alleigance
    global mission
    global fuel
    print('you are now in a station')
    x = True
    while x not in ['y', 'yes', 'n', 'no', blackMarketEntryCode]:
        x = input('do you wish to dock: y/n').lower()
        if x in ('y', 'yes'):
            t.sleep(0.5)
            while True:
                if input('input name of ship requesting docking:').lower() == 'hawken':
                    if input('input PIN:') == '3725':
                        if random.randint(1, 2) == 1:
                            print('docking request accepted')
                            break
                        else:
                            print('docking request denied')
                    else:
                        print('invalid PIN')
                        print('docking request denied')
            if input('do you want to buy an upgrade:Y/N').lower()in('y', 'yes'):
                x = upgrades
                choice1 = random.choice(x)
                x.remove(choice1)
                price1 = prices[choice1]
                if alleigance == 'foundation' and mapThree[system] > 0 and choice1 in ('electro-pulse', 'magnetic disintegrator'):
                    price1 -= 1
                if alleigance == 'empire' and mapThree[system] > 0 and choice1 in ('chaff', 'rapid fire'):
                    price1 -= 1
                choice2 = random.choice(x)
                price2 = prices[choice2]
                if alleigance == 'foundation' and mapThree[system] > 0 and choice2 in ('electro-pulse', 'magnetic disintegrator'):
                    price2 -= 1
                if alleigance == 'empire' and mapThree[system] > 0 and choice2 in ('chaff', 'rapid fire'):
                    price2 -= 1
                print('you can buy:')
                t.sleep(0.5)
                print('1.{0}:{1}'.format(choice1, descriptions[choice1]))
                print('price:{0} credits'.format(str(price1)))
                t.sleep(0.5)
                print('2.{0}:{1}'.format(choice2, descriptions[choice2]))
                print('price:{0} credits'.format(str(price2)))
                t.sleep(0.5)
                if credit == 0:
                    print('you are skint\nand cannot buy anything')
                elif credit == 1:
                    print('you have 1 credit\nand cannot buy anything')
                elif credit < prices[choice1] and credit < prices[choice2]:
                    print('you have {0} credits\nand cannot buy anything'.format(str(credit)))
                else:
                    print('you have {0} credits'.format(str(credit)))
                    choice = 0
                    while choice not in ['1', '1.', '2', '2.', 'N', 'n', choice2, choice1]:
                        choice = input('numeric input/name of upgrade/N to refuse to buy:')
                        if choice in ['1', '1.', choice1]:
                            if credit >= prices[choice1]:
                                print('you now have {0}'.format(choice1))
                                f.moves[choice1] = random.randint(18, 25)
                                GSK.moves[choice1] = random.randint(18, 25)
                                credit -= prices[choice1]
                            else:
                                print('sorry, but you don\'t have enough money')
                        elif choice in ['2', '2.', choice2]:
                            if credit >= prices[choice2]:
                                print('you now have {0}'.format(choice2))
                                f.moves[choice2] = random.randint(18, 25)
                                GSK.moves[choice2] = random.randint(18, 25)
                                credit -= prices[choice2]
                            else:
                                print('sorry, but you don\'t have enough money')
                        else:
                            print('invalid command')
            if fuel < 20 and credit >= round((20 - fuel)/5) and input('do you want to fill up on fuel({0} credits):Y/N'.format(str(round((20 - fuel)/5)))).lower() in ('y', 'yes'):
                credit -= round((20 - fuel)/5)
                fuel = 20
            if alleigance != 'neutral' and input('do you want to use the bulletin board:Y/N').lower() in ('y', 'yes'):
                if mission['target'] == system and mission['cargo'] in f.moves:
                    credit += mission['reward']
                    del f.moves[mission['cargo']]
                    mission['cargo'] = ''
                    if alleigance == 'empire':
                        mapThree[system] -= 1
                        print('thanks for helping the empire')
                    else:
                        mapThree[system] += 1
                        print('thanks for helping the foundation')
                m1 = {'target': random.choice(missionMap), 'cargo': random.choice(missionCargoes), 'reward': random.randint(1,5)}
                m2 = {'target': random.choice(missionMap), 'cargo': random.choice(missionCargoes), 'reward': random.randint(1,5)}
                m3 = {'target': random.choice(missionMap), 'cargo': random.choice(missionCargoes), 'reward': random.randint(1,5)}
                print('mission 1:')
                print('destination:{0}'.format(m1['target']))
                if m1['cargo'] == 'info':
                    if (alleigance == 'empire' and mapThree[system] < 0) or (alleigance == 'foundation' and mapThree[system] > 0):
                        print('cargo: military plans')
                    else:
                        print('cargo: secret intelligence')
                else:
                    print('cargo:{0}'.format(m1['cargo']))
                print('reward:{0}'.format(m1['reward']))
                print('mission 2:')
                print('destination:{0}'.format(m2['target']))
                if m2['cargo'] == 'info':
                    if (alleigance == 'empire' and mapThree[system] < 0) or (alleigance == 'foundation' and mapThree[system] > 0):
                        print('cargo: military plans')
                    else:
                        print('cargo: secret intelligence')
                else:
                    print('cargo:{0}'.format(m2['cargo']))
                print('reward:{0}'.format(m2['reward']))
                print('mission 3:')
                print('destination:{0}'.format(m3['target']))
                if m3['cargo'] == 'info':
                    if (alleigance == 'empire' and mapThree[system] < 0) or (alleigance == 'foundation' and mapThree[system] > 0):
                        print('cargo: military plans')
                    else:
                        print('cargo: secret intelligence')
                else:
                    print('cargo:{0}'.format(m3['cargo']))
                print('reward:{0}'.format(m3['reward']))
                while True:
                    Input = input('type mission number, or x to leave')
                    if Input in ('1', '1.'):
                        mission = m1
                        if m1['cargo'] == 'info':
                            f.moves['info'] = random.randint(1, 25)
                        break
                    if Input in ('2', '2.'):
                        mission = m2
                        if m2['cargo'] == 'info':
                            f.moves['info'] = random.randint(1, 25)
                        break
                    if Input in ('3', '3.'):
                        mission = m3
                        if m3['cargo'] == 'info':
                            f.moves['info'] = random.randint(1, 25)
                        break
                    if Input in ('x', 'X'):
                        break
            if bounty['empire' if mapThree[system] < 0 else  'foundation'] + bounty['general'] != 0 and credit >= bounty[
                'empire' if mapThree[system] < 0 else 'foundation'] + bounty['general'] and input(
                    'would you like to pay off your bounty Y/N: ').lower() == 'y':
                credit -= bounty['empire' if mapThree[system] < 0 else 'foundation'] + bounty['general']
                bounty['general'] = 0
                if mapThree[system] < 0:
                    bounty['empire'] = 0
                else:
                    bounty['foundation'] = 0
            if mapThree[system] > 0 and alleigance == 'neutral':
                print('help the foundation')
                print('join up today and get discounts on \nelectro-pulse and magnetic disintegration')
                if input('join the foundation:Y/N').lower() in ('yes', 'y'):
                    alleigance = 'foundation'
                    print('well done for choosing to prevent the age of barbarism')
            elif mapThree[system] < 0 and alleigance == 'neutral':
                print('help the empire')
                print('join up today and get discounts on \nrapid fire and magnetic disintegration')
                if input('join the empire:Y/N').lower() in ('yes', 'y'):
                    alleigance = 'empire'
                    print('well done for choosing to stop the rise of the upstart foundation')
        elif x in ('n', 'no'):
            return
        elif x == blackMarketEntryCode:
            for i in f.moves:
                if i in blackCommodities:
                    del f.moves[i]
                    credit += blackCommodities[i] + random.randint(1,3)
        else:
            print('invalid command')
def fightBack():
    global alliegance
    global missionMap
    system = random.choice(missionMap)
    if alleigance == 'empire':
        mapThree[system] += 1
    elif alleigance == 'foundation':
        mapThree[system] -= 1
def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def gS(curSys):
    global credit
    GSK.main()
    if GSK.winner == 'player':
        mapTwo[curSys].remove('gS({0})'.format(curSys))
        credit += 10
    if GSK.winner == 'none':
        choice = random.choice(mapOne[curSys])
        mapTwo[choice].insert(random.randint(0, len(mapTwo[choice]), 'gS({0})'.format(choice)))
        mapTwo[curSys].remove('gS({0})'.format(curSys))
def hyperDrive(sysTarg):
    t.sleep(0.5)
    print('initialising energy streams')
    t.sleep(0.75)
    print('targeting {0}'.format(sysTarg))
    t.sleep(1)
    print('opening power gates')
    t.sleep(1.25)
    while True:
        if input('input PIN:') == '3725':
            break
        else:
            print('invalid password, try again')
    print('''     #~~~~#
   #--------#
 #____________#
#¬¬¬¬¬¬¬¬¬¬¬¬¬¬#
 #____________#
   #--------#
     #~~~~#''')
def gPlanet():
    print('you are now in orbit around a gas giant')
def rPlanet(system):
    global credit
    print('you are now in orbit around a rocky planet')
    orbitingShips = {'federal logistics': random.randrange(0, 2, 3), 'combat': random.randrange(0, 2 if system == 'tazenda' else 1, 3), 'freight': random.randrange(0, 1 if system == 'tazenda' else 2, 2 if system == 'tazenda' else 4)}
    if orbitingShips['federal logistics'] + orbitingShips['combat'] + orbitingShips['freight'] == 0:
        print('there are no ships in orbit around this planet')
    else:
        print('ships:')
        for i in orbitingShips:
            print('{0}:{1}'.format(i, str(orbitingShips[i])))
        if ((mapThree[system] > 0 and bounty['foundation'] > random.randrange(4, 2, 1)) or (mapThree[system] < 0 and bounty['empire'] > random.randrange(4, 2, 1)) or (bounty['general'] > random.randrange(4, 2, 1))) and orbitingShips['combat'] > 0:
            fightZone('n', system)
        while True:
            if input('do you want to fight Y/N: ').lower() == 'y':
                while x not in ('freight', 'federal logistics', 'combat'):
                    x = input('what type of ship do you want to attack: ').lower()
                if x == 'freight' and orbitingShips['freight'] != 0:
                    if random.randint(1, 50 if len(f.moves) == 3 else 50*(len(f.moves) - 3)) == 1:
                        print('you were defeated by a freight ship, and now the denizens\n of the galaxy will look on you in shame')
                        s.exit()
                    else:
                        y = random.randint(1, 5)
                        credit += y
                        bounty['general'] += y + 1
                        print('you defeated the ship, and after selling it\'s cargo on Gbay\nyou have made {0} credits, however you also aquired a general\nbounty of {1} credits'.format(str(y), str(y + 1)))
                        orbitingShips['freight'] -= 1
                elif x == 'federal logistics' and orbitingShips['federal logistics'] != 0:
                    if random.randint(1, 20 if len(f.moves) == 3 else 20*(len(f.moves) - 3)) == 1:
                        print('you were defeated by a federal logistics ship, but a failure here is not to terrible \nfor they carry messages of the utmost sensitivity, and must protect them well')
                        s.exit()
                    else:
                        y = random.randint(3, 6)
                        bounty['general'] += y
                        print('you defeated the ship, and have aquired a state bounty of {0}.'.format(y))
                        if alleigance == 'empire':
                            mapThree[system] -= 1
                        elif alleigance == 'foundation':
                            mapThree[system] += 1
                        orbitingShips['federal logistics'] -= 1
                elif x == 'combat' and orbitingShips['combat'] != 0:
                   fightZone('y', system)
                else:
                    print('invalid action.')
            else:
                break
def main(curSys, curRad):
    global credit
    global fuel
    class pirateShip():
        def __init__(self, name, reckless, knowledge, sys, rad):
            self.reckless = reckless
            self.name = name
            self.knowledge = knowledge
            self.sys = sys
            self.rad = rad
            self.entered = False
        def move(self):
            for i in range(3):
                choices = mapOne[curSys]
                if self.reckless() > len(choices):
                    choices = choices[:self.reckless - 1]
                else:
                    choices = [choices[1]]
                choice = random.choice(choices)
                mapTwo[choice].insert(random.randint(0, len(mapTwo[choice]), '{0}.enter()'.format(self.name)))
                mapTwo[curSys].remove('{0}.enter()'.format(self.name))
                if self.entered:
                    t.sleep(0.5)
                    print('initialising energy streams')
                    t.sleep(0.75)
                    print('targeting {0}'.format(choice))
                    t.sleep(1)
                    print('opening power gates')
                    t.sleep(1.25)
                    print('input PIN: ' end='')
                    for i in range(4):
                        t.sleep(0.5)t.sleep(0.25)
                        print('*' end='')
                    print('''     #~~~~#
                       #--------#
                     #____________#
                    #¬¬¬¬¬¬¬¬¬¬¬¬¬¬#
                     #____________#
                       #--------#
                         #~~~~#''')
        def enter(self):
            print('you are now near a pirate ship')
            if input('do you wish to dock: y/n').lower in ('y', 'yes'):
                t.sleep(0.5)
                while True:
                    if input('input name of ship requesting docking:').lower() == 'hawken':
                        if input('input PIN:') == '3725':
                            if random.randint(1, 2) == 1:
                                print('docking request accepted')
                                break
                            else:
                                print('docking request denied')
                        else:
                            print('invalid PIN')
                            print('docking request denied')
                self.entered = True
            else:
                orbitingShips = {'combat': random.randrange(0, 2 if self.sys == 'tazenda' else 1, 3)}
                if orbitingShips['combat'] == 0:
                    print('there are no ships in near this ship')
                else:
                    print('ships:')
                    for i in orbitingShips:
                        print('{0}:{1}'.format(i, str(orbitingShips[i]))
                    if ((mapThree[self.sys] > 0 and bounty['foundation'] > random.randrange(4, 2, 1)) or (
                            mapThree[self.sys] < 0 and bounty['empire'] > random.randrange(4, 2, 1)) or (
                        bounty['general'] > random.randrange(4, 2, 1))) and orbitingShips['combat'] > 0:
                        fightZone('n', self.sys)
                    while True:
                        if input('do you want to fight Y/N: ').lower() in ('y', 'yes'):
                            fightZone('y', self.sys)
                            orbitingShips['combat'] -= 1
                        else:
                            break
            if self.entered:
                print('welcome to the bad ship {0}'.format(self.name))
                if input('do you want to enter the black market:Y/N ').lower() in ('y', 'yes'):
                    item1 = random.choice(blackCommodities)
                    x = blackCommodities
                    x.remove(item1)
                    item2 = random.choice(x)
                    for i in item1:
                        trueI1 = i
                        valOfI1 = item1[i]
                    for i in item2:
                        trueI2 = i
                        valOfI2 = item2[i]
                    if credit < valOfI2 or credit < valOfI1:
                        print('you cannot buy anything')
                    print('you can buy the following black market items:')
                    print('you can buy:')
                    for i in item1:
                        print('1){0}:{1}'.format(i, str(item1[i])))
                    for i in item2:
                        print('2){0}:{1}'.format(i, str(item2[i])))
                    while True:
                        if credit < valOfI2 or credit < valOfI1:
                            print('you cannot buy anything')
                            break
                        decision = input('which item do you want to buy(numerical)? ')
                        if decision.lower() in ('1', '1.', '1)'):
                            if credit >= valOfI1:
                                print('you now have {0}'.format(trueI1))
                                f.moves[trueI1] = random.randint(18, 25)
                                GSK.moves[trueI1] = random.randint(18, 25)
                                credit -= valOfI1
                                break
                        if decision.lower() in ('2', '2.', '2)'):
                            if credit >= valOfI2:
                                print('you now have {0}'.format(trueI2))
                                f.moves[trueI2] = random.randint(18, 25)
                                GSK.moves[trueI2] = random.randint(18, 25)
                                credit -= valOfI2
                                break
                        else:
                            print('invalid command')
                    blackMarketEntryCode = str(random.randint(1000, 9999))
                    print('''when it asks you if you want to dock
                    type in this number: {0}. it will then offload
                     all your black market goods at a profit.''')

    go = 0
    print('from the mind of fred powell')
    t.sleep(2)
    print('with thanks to a person on stack exchange called quill')
    t.sleep(2)
    print('we present:')
    print()
    t.sleep(2)
    print('#------------------#')
    print()
    print('#castles in the sky#')
    print()
    print('#------------------#')
    t.sleep(3)
    for i in range(45):
        print()
    print('''you are captain of the good ship
hawken. you are crossing the galaxy, with
no particular aim in mind other than to
have fun.
your personal ID number is
'3725'
good luck captain''')
    while True:
        print('you are in the system of {0}'.format(curSys))
        t.sleep(0.5)
        if curRad == 1:
            print('your stellar radius is 1 orbital field from system centre')
        else:
            print('your stellar radius is {0} orbital fields from system centre'.format(curRad))
        if curSys == 'sagitarius':
            print('you suddenly realise', end=', ')
            t.sleep(1.5)
            print('you are on the brink of a black hole.')
            t.sleep(0.5)
            print('you try to fight it, ', end='')
            t.sleep(0.5)
            print('but you are already passed the point of no return.')
            t.sleep(1.5)
            print('you are losing conciousness, ', end='')
            t.sleep(0.5)
            print('when suddenly')
            t.sleep(4)
            print('''     #~~~~#
   #--------#
 #____________#
#¬¬¬¬¬¬¬¬¬¬¬¬¬¬#
 #____________#
   #--------#
     #~~~~#''')
            print('T', end='')
            t.sleep(0.3)
            print('O', end='')
            t.sleep(0.3)
            print(' ', end='')
            t.sleep(0.3)
            print('B', end='')
            t.sleep(0.3)
            print('E', end='')
            t.sleep(0.3)
            print(' ', end='')
            t.sleep(0.3)
            print('C', end='')
            t.sleep(0.3)
            print('O', end='')
            t.sleep(0.3)
            print('N', end='')
            t.sleep(0.3)
            print('T', end='')
            t.sleep(0.3)
            print('I', end='')
            t.sleep(0.3)
            print('N', end='')
            t.sleep(0.3)
            print('U', end='')
            t.sleep(0.3)
            print('E', end='')
            t.sleep(0.3)
            print('D', end='')
            t.sleep(0.3)
            print('.', end='')
            t.sleep(0.5)
            print('.', end='')
            t.sleep(0.5)
            print('.')
            t.sleep(0.5)
            s.exit()
        t.sleep(0.5)
        if credit == 0:
            print('you are skint')
        elif credit == 1:
            print('you have 1 credit')
        else:
            print('you have {0} credits'.format(str(credit)))
        print('you have the following bounty\'s on your head')
        for i in bounty:
            print('{0}:{1}'.format(i, bounty[i]))
        a = mapTwo[curSys]
        b = a[curRad]
        if b == 'gs({0})'.format(curSys):
            if curRad != 0:
                curRad -= 1
            else:
                curRad += 1
        eval(b)
        t.sleep(0.5)
        leave = 'o'
        while leave.lower() not in(('y', 'n')):
            leave = input('do you want to leave the system of {0}:Y/N'.format(curSys))
            if leave == 'Y' or leave == 'y':
                if fuel >= 2:
                    t.sleep(0.5)
                    print('these are the systems you can go to.')
                    for i in range(len(mapOne[curSys])):
                        t.sleep(0.5)
                        c = mapOne[curSys]
                        d = c[i]
                        if mission['target'] == d:
                            print('mission target.')
                        print('{0}. {1}'.format(i, d))
                    while True:
                        x = input('''numeric commands with no
    dot/name of system please:''')
                        if isNumber(x) == True and int(x) <= len(c) and int(x) >=0:
                            y = int(x)
                            hyperDrive(c[y])
                            curSys = c[y]
                            curRad = 0
                            fuel -= 2
                            break
                        elif x in c:
                            hyperDrive(x)
                            curSys = x
                            curRad = 0
                            fuel -= 2
                            break
                        else:
                            t.sleep(0.5)
                            print('invalid command')
                    else:
                        print('not enough remaining fuel')
                       
            elif leave.lower() in ('n', 'no'):
                print('you can do any of the following')
                t.sleep(0.5)
                print('1.stay')
                n = 1
                t.sleep(0.5)
                if fuel >= 1:
                    for i in range(1):
                        if curRad == 0:
                            n = 2
                            break
                        print('2.lower stellar radius')
                        n = 3
                        t.sleep(0.5)
                    for i in range(1):
                        if curRad == (len(mapTwo[curSys])) - 1:
                            break
                        print('{0}.raise stellar radius'.format(n))
                        t.sleep(0.5)
                    x = input('numeric input, no dot, only:')
                if isNumber(x) == True and int(x) <= n and int(x) >= 1:
                    if x == '2':
                        if curRad == 0:
                            curRad += 1
                            fuel -= 1
                        else:
                            curRad -=1
                            fuel -= 1
                    if int(x) == 3:
                        curRad += 1
                        fuel -= 1
                else:
                    print('invalid command')
            else:
                t.sleep(0.5)
                print('invalid command')
        go += 1
        if go == 3:
            fightBack()
            go = 0
main('anacreon', 0)
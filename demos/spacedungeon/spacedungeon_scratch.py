import random


##player = {
##'HP': 100,
##'attack': 100,
##'defense': 100
##}
##
##enemy1 = {
##'HP': 100,
##'attack': 100,
##'defense': 100,
##}
##
##
##

def get_item(player):
    item_list = ["MRE", "First Aid Kit", "Meth-derived stim-pack"]

    print("You find a ", item_list[random.randint(0,2)],
    "your health increased by ", (abs(player['HP'] - 100)), "HP")

    return player['HP'] += abs(player['HP'] - 100)

def attack(opponent):
    rand_damage = random.randint(8,32)
    opponent['HP'] -= rand_damage
##    if opponent['HP'] <= 0:
##        opponent['HP'] = 0
##        return opponent
    ##print(opponent['HP'])
##    else:
    return opponent

def fight(oppo1, oppo2):
    while (oppo1['HP'] > 0) and (oppo2['HP'] > 0) == True:
        attack(oppo2)
        if oppo2['HP'] <= 0:
            print("oppo1 is winner")
        else:
            attack(oppo1)
        if oppo1['HP'] <= 0:
            print("oppo2 is winner")

##        if oppo1['HP'] > 0:
##            attack(oppo2)
##        else:
##            pass
##    if oppo1['HP'] <= 0:
####        if oppo1['HP'] <= 0:
####            oppo1['HP'] = 3
##        return print("oppo2 is winner")
##    elif oppo2['HP'] <= 0:
####        if oppo2['HP'] <= 0:
####            oppo2['HP'] = 3
##        return print("oppo1 is winner")
##    else:
##        print("something went south")
    
def main():

    player = {
'HP': 80,
'attack': 100,
'defense': 100
}

    enemy1 = {
'HP': 100,
'attack': 100,
'defense': 100,
}

##    fight(player, enemy1)
    get_item(player)
    print('player1 oppo1 HP: ', player['HP'])
    print('enemy1  oppo2 HP: ', enemy1['HP'])

    
##    attack(enemy1)
##    print(enemy1['HP'])

main()

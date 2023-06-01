import random
from dice import WoodDice, Dice , RiggedDice
from character import Character, Warrior, Mage, Thief, Wolf, Bat
from rich import print 
from message import Message



if (__name__ == "__main__"):
    
    warrior = Warrior("Igrith", 20, 8,3, Dice())
    mage = Mage("Merlin", 20, 8,3, Dice())
    thief = Thief("Boubou", 20, 8,3, Dice())

    wolf = Wolf("Tommy The Wolf", 20, 8,3, Dice())
    bat = Bat("Xerath The Bat", 20, 8,3, Dice(4))

    cars = [mage, warrior, thief]
    stats = {}

    enemies = [wolf,bat]

    Message.start_prompt()
    choice = Message.caracter_choice()

    user_car = cars[choice - 1]

    run = 0
    

    while (len(enemies)>0 and user_car.is_alive()):
        run += 1
        enemy = random.choice(enemies)
        enemies.remove(enemy)

        Message.run_intro(enemy.name)

        while(user_car.is_alive() and enemy.is_alive()):
            user_car.attack(enemy)
            enemy.attack(user_car)
        if(user_car.is_alive()):
            Message.run_win()
        elif(enemy.is_alive()):
            Message.run_lose()
    if (user_car.is_alive()):
        Message.win()
    

        
    # cars.remove(car_1)

    # car_2 = random.choice(cars)
    # cars.remove(car_2)

    # print(cars, car_1, car_2, sep='/n')

    # stats[car_1.get_name()] = 0

    # stats[car_2.get_name()] = 0

    # print (stats)

    
    # car_1.regenerate()
    # car_2.regenerate()
    # while(car_1.is_alive() and car_2.is_alive()):
    #     car_1.attack(car_2)
    #     car_2.attack(car_1)
    # if(car_1.is_alive()):
    #     stats[car_2.get_name()]+= 1

    # elif(car_2.is_alive()):
    #     stats[car_1.get_name()]+= 1



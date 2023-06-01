from dice import Dice, WoodDice, RiggedDice
from rich import print
from message import Message

class Health :
    pass
class Action : 
    pass
class Character:
    label = "Character"
    def __init__(self, name, max_health, attack, defense ,dice ):

        self.name = name
        self.max_health = max_health
        self.health = self.max_health
        self.attack_value = attack
        self.defense_value = defense
        self.dice: Dice = dice
        self.message = Message(self.name,self.max_health,self.attack_value,self.defense_value,type(self).label)
    
    def __str__(self):
        return f"I'm {self.name} a {type(self).label} with  {self.health}/{self.max_health} HP"
    def get_type(self):
        return type(self).label
    def get_name(self):
        return self.name
    
    def regenerate(self):
        self.health = self.max_health
    def is_alive(self):
        return self.health > 0
    
    def compute_damage(self,roll,target=None):
        return self.attack_value + roll
    
    def still_health(self,target, health_point):
        target.health -= health_point
        self.health += health_point



    def compute_wound(self,damages,roll,attacker=None):
        return damages - self.defense_value - roll
    
    
    def affect_health(self, amount):
        self.health -= (amount)
        # Fix temporaire : class health necessaire à l'avenir 
        # #gestion de la vie 
        if self.health < 0 :
            self.health = 0

        self.message.display_healthbar(self.health)

    def attack(self, target):
        if (self.is_alive() and target.is_alive()):
            roll = self.dice.roll()
            damages =  self.compute_damage(roll, target)
            self.message.attack(target.name,damages ,roll)
            target.defend(damages, self)

    
    def defend(self, damages, attacker):
        roll = self.dice.roll()
        wounds = self.compute_wound(damages,roll, attacker)
        if (wounds < 0):
            self.message.defense(attacker.name, damages, wounds, roll)
            wounds = 0
        self.affect_health(wounds)

class Warrior(Character):
    label = "[italic red]Warrior[/italic red]"
    def compute_damage(self, roll, target):
        self.message.bonus("Ax 🪓 ", "+3")
        return super().compute_damage(roll) + 3

class Mage(Character):
    label = "[italic blue]Mage[/italic blue]"
    def compute_wound(self,damages, roll, attacker):
        self.message.bonus("Magic shield 🔮", "-3")
        return super().compute_wound(damages, roll)  - 3

class Thief(Character):
    label = "[italic green]Thief[/italic green]"
    # ignore defense de l'adversaire 
    def compute_damage(self, roll, target):
        damages = super().compute_damage(roll) + target.defense_value
        self.message.bonus("Sneaky knife 🔪", f"+{damages}")
        return damages
    
class Wolf(Character):
    label = "[italic grey]Wolf[/italic grey]"
    def compute_damage(self, roll, target):
        physic_bonus = type(target) == Warrior
        damages = super().compute_damage(roll) + 3 if physic_bonus else 0
        self.message.bonus("Sharp teeth 🦷", f"+{damages}")
        return damages
    
class Bat(Character):
    label = "[italic grey]Bat[/italic grey]"
    def compute_damage(self, roll, target):
        magic_bonus = type(target) == Mage
        damages = super().compute_damage(roll) + 3 if magic_bonus else 0
        self.message.bonus("Vampire dodge 🩸", f"+{damages}")
        self.still_health(target,4)
        return damages
    

if (__name__  == "__main__"):  

    pass





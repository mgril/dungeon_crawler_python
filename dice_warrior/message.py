from rich import print

class Message :
    def __init__(self, name, max_health, attack_value, defense_value, label):
        self.name = name
        self.label = label
        self.max_health = max_health
        self.attack_value = attack_value
        self.defense_value = defense_value

    def display_healthbar(self,health):
        print(f"[{'💚'* health}{'🤍'*(self.max_health -health)}] {health}/{self.max_health}  :  {self.label} {self.name} point health")

    def attack(self, name_target,damages ,roll):
        print(f"🗡️ {self.label} {self.name} attack {name_target} with {damages} damages (attack : {self.attack_value} + roll : {roll})")

    def defense(self, name_attacker, damages, wounds, roll):
        print( f"🛡️ {self.label} {self.name} defend against {name_attacker} with {damages} damages and takes {wounds} wounds (defense: {self.defense_value} + roll: {roll})")

    def bonus(self,bonus_item, damages):
        print (f"Bonus : {bonus_item} 🔮 ({damages} Damages)")
    

    @staticmethod
    def start_prompt():
        
        print("Bienvenue dans la mystérieuse forêt enchantée ! Prépare-toi à t'embarquer dans une aventure épique au cœur de ce royaume de verdure luxuriante. Entouré d'arbres majestueux et de créatures fantastiques, tu es sur le point de vivre des moments inoubliables.")

        pass_intro = input("Voulez vous passer l'intro y/n")
        if (pass_intro == "n"):
            print("Au-delà des sentiers battus, tu découvriras peut-être des secrets anciens, des énigmes à résoudre ou même des personnages étonnants prêts à t'aider dans ta quête. Reste vigilant, car chaque pas que tu franchis peut t'ouvrir de nouvelles perspectives sur cette terre mystique.")
            input()
            print("Que tu sois un aventurier intrépide ou simplement en quête de tranquillité, cette forêt t'offre une expérience unique. Prépare-toi à explorer ses recoins, à rencontrer des créatures étranges et à t'immerger dans un univers enchanteur où l'imagination est la clé.")
            input()
            print("Maintenant, fais preuve de courage et d'audace, cher voyageur, et lance-toi dans cette incroyable aventure au cœur de la forêt enchantée ! Que la magie te guide et que chaque instant passé ici soit empreint de merveilles sans fin. Bon jeu !")
            input()
        

    @staticmethod   
    def caracter_choice():
        caracters = ["Mage","Combattant","Voleur"]
        choice = input(" Preferes tu être \n 1 - un Mage \n 2 - un Combattant \n 3 - un Voleur \n Inscrit le numéro correspondant à ton choix")
        while(choice != "1" and choice !="2" and choice !="3"):
            print("Le nombre entré n'est pas bon")
            choice = input("  Preferes tu être \n 1 - un Mage \n 2 - un Combattant \n 3 - un Voleur \n Inscrit le numéro correspondant à ton choix \n")
        print(f"Vous avez choisi un {caracters[int(choice)-1]}")    
        return int(choice)
    
    @staticmethod   
    def run_intro(enemy_name):
        print(f"Oh non tu as rencontré {enemy_name}")
        input()

    @staticmethod   
    def run_win():
        print("Bien joué tu as survécu à ce run \n Passer au run suivant")
        input()

    @staticmethod 
    def run_lose():
        print("Tu n'es peut être pas très bon tu es mort l'aventure s'arrête ici")

    @staticmethod 
    def win():
        print("Bien joué tu as vaincu tout les ennemies")

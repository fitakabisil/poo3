import random

# numéro d'attribu
lancer_dé1 = random.sample(range(1, 6), 4)  # faire lancer 4 dé à 6 faces et mettre ca dans un list
lancer_dé1.remove(min(lancer_dé1))  # enlever le nombre le plus petit de la list
Sum1 = sum(lancer_dé1)  # additioner le rest des nombres dans la list et le transformer en integer

lancer_dé2 = random.sample(range(1, 6), 4)
lancer_dé2.remove(min(lancer_dé2))
Sum2 = sum(lancer_dé2)

lancer_dé3 = random.sample(range(1, 6), 4)
lancer_dé3.remove(min(lancer_dé3))
Sum3 = sum(lancer_dé3)

lancer_dé4 = random.sample(range(1, 6), 4)
lancer_dé4.remove(min(lancer_dé4))
Sum4 = sum(lancer_dé4)

lancer_dé5 = random.sample(range(1, 6), 4)
lancer_dé5.remove(min(lancer_dé5))
Sum5 = sum(lancer_dé5)

lancer_dé6 = random.sample(range(1, 6), 4)
lancer_dé6.remove(min(lancer_dé6))
Sum6 = sum(lancer_dé6)


class NPC:  # création de la class

    def __init__(self):  # définition des attribues
        self.Force = Sum1

        self.Agilité = Sum2

        self.Constitution = Sum3

        self.Intelligence = Sum4

        self.Sagesse = Sum5

        self.Charisme = Sum6

        self.class_armure = random.randint(1, 12)

        self.points_vie = random.randint(1, 20)

        self.nom = "Joe Gulivan"

        self.race = 'Human'

        self.profession = 'fermier'

    def print_stats(self):  # donner l'accès au attribues

        print('stats NPC:')
        print('Force:', self.Force)
        print('Agilité:', self.Agilité)
        print('Constitution:', self.Constitution)
        print('Intelligence:', self.Intelligence)
        print('Sagesse:', self.Sagesse)
        print('Charisme:', self.Charisme)
        print('Nom:', self.nom)
        print("Classe de l'armure:", self.class_armure)
        print('Points de Vie:', self.points_vie)
        print('Race:', self.race)
        print('Profession:', self.profession)


print(NPC().print_stats())  # affichage des attribues


class Kobold(NPC):  # création des classes enfants

    def __init__(self, ):
        super(Kobold, self).__init__()  # donner les attribues de la classe NPC au classes enfants

    def attaquer(self, npc):  # méthode attaquer de la class kobold

        lancer_dék = random.randint(1, 20)

    def subir_domage(self):  #méthode subir domage de la class kobold
        
    # les points de vies du kobold sont les points d'attaque du héro soustrait des PV de la classe NPC
        self.points_vie = Hero.attaquer()


class Hero(NPC):

    def __int__(self):
        super().__init__()

        self.lancer_déh: random.randint(1, 20)  # represent la chance d'attaque du héro

        self.subir_dom = 1

    def attaquer(self, kobold, lancer_déh):  # méthode attaquer du héro

        lancer_déh = self.lancer_déh

        if lancer_déh == 20:  # si le lancer de dé = 20, le héro va avoir une attaque critique

            kobold.points_vie(random.randint(1, 8))  # soustraction de PV du kobold de 1 à 8

    def subir_domage(self, subir_dom): # méthode subir domage du héro

        if NPC(self.points_vie) == 0: # j'ai mis n'import quoi. Si les PV de la classe NPC = 0 le héro meurt

            print('{NPC est mort}')
            

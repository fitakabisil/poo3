import random

# numéro d'attribue
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

        self.nom = "Joe Gulivsn"

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

    def __init__(self):
        super(Kobold, self).__init__()

    def attaquer(self, attaque_k):

        attaque_k = random.randint(1, 20)

    def subir_domage(self):

        self.subir_domage = Hero.attaquer()


class Hero(NPC):

    def attaquer(self, attaque_h):

        print(Hero.attaquer())

        attaque_h = random.randint(1, 20)

    def subir_domage(self, subir_domage):

        subir_domage: int

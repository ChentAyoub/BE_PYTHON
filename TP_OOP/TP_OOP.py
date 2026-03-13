from abc import ABC, abstractmethod
from dataclasses import dataclass

class Boisson(ABC):
    @abstractmethod
    def cout(self):
        pass

    @abstractmethod
    def description(self):
        pass
    
    def __add__(self, other): 
        if isinstance(other, Boisson):
            return BoissonCombinee(self, other)

class BoissonCombinee(Boisson):
    def __init__(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        
    def cout(self):
        return self.b1.cout() + self.b2.cout()
        
    def description(self):
        return self.b1.description() + " + " + self.b2.description()

class Cafe(Boisson):
    def cout(self): return 2.0
    def description(self): return "Café simple"

class The(Boisson):
    def cout(self): return 1.5
    def description(self): return "Thé"

class DecorateurBoisson(Boisson):
    def __init__(self, boisson):
        self._boisson = boisson

class Lait(DecorateurBoisson):
    def cout(self): return self._boisson.cout() + 0.5
    def description(self): return self._boisson.description() + ", Lait"

class Sucre(DecorateurBoisson):
    def cout(self): return self._boisson.cout() + 0.2
    def description(self): return self._boisson.description() + ", Sucre"

class Caramel(DecorateurBoisson):
    def cout(self): return self._boisson.cout() + 0.7
    def description(self): return self._boisson.description() + ", Caramel"

@dataclass
class Client:
    nom: str
    numero: int
    points_fidelite: int = 0

class Commande:
    def __init__(self, client):
        self.client = client
        self.boissons = []

    def ajouter_boisson(self, boisson):
        self.boissons.append(boisson)

    def prix_total(self):
        return sum(b.cout() for b in self.boissons)

    def afficher(self):
        print(f"\n--- Commande de {self.client.nom} ---")
        for b in self.boissons:
            print(f"Commande: {b.description()}")
            print(f"Prix: {b.cout():.2f}€\n")
        print(f"TOTAL DE LA COMMANDE : {self.prix_total():.2f}€")

class CommandeSurPlace(Commande):
    def afficher(self):
        print("\n[ Mode : SUR PLACE ]")
        super().afficher()

class CommandeEmporter(Commande):
    def afficher(self):
        print("\n[ Mode : À EMPORTER ]")
        super().afficher()

class Fidelite:
    def ajouter_points(self, client, montant):
        points = int(montant)
        client.points_fidelite += points
        print(f"⭐ Vous avez gagné {points} points ! (Nouveau solde : {client.points_fidelite} pts)")

class CommandeFidele(Commande, Fidelite):
    def valider(self):
        self.afficher()
        self.ajouter_points(self.client, self.prix_total())

if __name__ == "__main__":
    client1 = Client(nom="Ahmed", numero=101)

    boisson1 = Sucre(Lait(Cafe()))
    boisson2 = Caramel(The())
    boisson_combinee = Cafe() + The()

    ma_commande = CommandeFidele(client1)

    ma_commande.ajouter_boisson(boisson1)
    ma_commande.ajouter_boisson(boisson2)
    ma_commande.ajouter_boisson(boisson_combinee)

    ma_commande.valider()
import math

class Table_hachage_Mul:

    def __init__(self):
        self.taille = 10
        self.affichage = [[] for _ in range(0, self.taille)]

    #fonction de multiplication
    def fonction_multiplication(self, cle):
        nb_d_orr = 0.6125423371
        n = int(cle)
        mod = math.floor(((n*nb_d_orr) % 1)*self.taille)
        return mod

    def set(self, cle, valeur):
        hachage = self.fonction_multiplication(cle)
        cle_existant = False
        slot = self.affichage[hachage]
        for i, kv in enumerate(slot):
            k, v = kv
            if cle == k:
                cle_existant = True
                break

        if cle_existant:
            slot[i] = ((cle, valeur))
        else:
            slot.append((cle, valeur))

    def get(self, cle):
        hachage = self.fonction_multiplication(cle)
        slot = self.affichage[hachage]
        for kv in slot:
            k, v = kv
            if cle == k:
                return v
            else:
                raise KeyError('Désolé ! cette clé n\'existe pas.')

    def __setitem__(self, cle, valeur):
        return self.set(cle, valeur)

    def __getitem__(self, cle):
        return self.get(cle)

#Les valeurs de test
H1 = Table_hachage_Mul()

H1.set(1,'2018')
H1.set(2,'2019')
H1.set(3,'2020')
H1.set(4,'2021')
H1.set(5,'2022')
H1.set(6,'2022')
H1.set(8,'2022')

H1.set(6,'SRIT')
H1.set(7,'SIGL')
H1.set(8,'RTEL')
H1.set(9,'TWIN')
H1.set(10,'DASI')

#print(H1.affichage)
class Table_hachage:

    def __init__(self):
        self.taille = 10
        self.affichage = [[] for _ in range(0, self.taille)]

    def fonction_hachage(self, cle):
        cle_hachee = hash(cle) % self.taille
        return cle_hachee

    def set(self, cle, valeur):
        hachage = self.fonction_hachage(cle)
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
        hachage = self.fonction_hachage(cle)
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
H = Table_hachage()

H.set('cle1','Master MBDS')
H.set('cle2','Master BIHAR')
H.set('cle3','Master RTEL')
H.set('cle4','Master INFO')
H.set('cle5','Master ERIS')

H.set(1,'2018')
H.set(2,'2019')

#print(H.affichage)
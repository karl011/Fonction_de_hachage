from table_hachage_multiplication import *
from table_hachage_division import *

def comptageCollisionDivision():
    compteurDiv = 0
    for i in H.affichage:
        if len(i) > 1:
            val = len(i)-1
            compteurDiv = compteurDiv + val
    return compteurDiv

def comptageCollisionMultip():
    compteMultip = 0
    for i in H1.affichage:
        if len(i) > 1:
            val = len(i)-1
            compteMultip = compteMultip+val
    return compteMultip

testDiv = comptageCollisionDivision()
testMul = comptageCollisionMultip()
print
if testDiv > testMul:
    print("-----------Affichage de la table de hachage de multiplication-------------")
    print()
    print(H1.affichage)
    print()
    print("La multiplication est la fonction avec le plus de collisions avec", testMul )
elif testDiv == testMul:
    print("Les deux fonctions le même nombre de collisions")
else:
    print("-----------Affichage de la table de hachage de division------------------")
    print()
    print(H.affichage)
    print()
    print("La division est la fonction avec le plus de collisions avec", testDiv)
def transform(chain):
    set_entiers = set()

    # Retrouve chaque entier sans doublon
    for items in chain:
        entiers = items.split(", ")
        for item in entiers:
            set_entiers.add(int(item))

    # Nouvelle chaine ordre croissanr
    entier_ordre = sorted(set_entiers)



    # Renvoie d'une nouvelle chaine tel que dans l'exemple
    set1 = set(map(int, chain[0].split(", ")))
    set2 = set(map(int, chain[1].split(", ")))
    entier_commun = sorted(set1.intersection(set2), reverse=True)

    if len(entier_commun) == 0:
        return None

    # Concactenation entre le nom prenom et la classe
    result = ",".join(map(str, entier_commun))
    result += ":NGUIMA-OSSIKETE_KenKleven_Master"

    return result

if __name__ == "__main__":
    arr1 = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
    out = transform(arr1)
    print(out)  # doit afficher ---> 1,2,3,4,7,13,15:nom_prenom_classe

    arr3 = ["9, 3, 5, 7, 14", "10, 2, 6, 16, 15"]
    out = transform(arr3)
    print(out)  # doit afficher ---> 2,3,5,6,7,9,10,14,15,16:nom_prenom_classe

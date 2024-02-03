import sqlite3

def nombre_manquant(tableau):
    # Somme Total des nombres consécutifs
    somme_total = sum(range(min(tableau), max(tableau) + 1))

    # Somme réelle des nombres dans le tableau
    somme_reelle = sum(tableau)

    # Trouver le nombre manquant
    nmbr_manquant = somme_total - somme_reelle

    # Stocker en SQLite
    con = sqlite3.connect('nombre1.db')
    curseur = con.cursor()
    curseur.execute('CREATE TABLE IF NOT EXISTS nombres_manquant (nombre INTEGER)')
    curseur.execute('INSERT INTO nombres_manquant VALUES (?)', (nmbr_manquant,))
    con.commit()
    con.close()

    return nmbr_manquant


tableau = [1, 2, 4, 5, 6, 7, 8]
print("Le nombre manquant est :", nombre_manquant(tableau))

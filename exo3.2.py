import sqlite3

def nombre_manquant(tableau):
    ensemble_nombres = set(tableau)

    # Trouver le nombre manquant
    for nombre in range(min(tableau), max(tableau)):
        if nombre not in ensemble_nombres:
            nmbr_manquant = nombre
            break

    # Stocker en SQLite
    con = sqlite3.connect('nombre2.db')
    curseur = con.cursor()
    curseur.execute('CREATE TABLE IF NOT EXISTS nombres_manquant (nombre INTEGER)')
    curseur.execute('INSERT INTO nombres_manquant VALUES (?)', (nmbr_manquant,))
    con.commit()
    con.close()

    return nmbr_manquant

tableau_test = [1, 2, 3, 4, 5, 7, 8]
print("Le nombre manquant est :", nombre_manquant(tableau_test))

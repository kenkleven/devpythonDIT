import sqlite3
import numpy as np

def nombre_manquant(tableau):
    ensemble_nombres = set(tableau)

    # Trouver le nombre manquant
    nmbr_manquant = next(num for num in range(np.min(tableau), np.max(tableau)) if num not in ensemble_nombres)

    # Stocker en SQLite
    con = sqlite3.connect('nombre2.db')
    curseur = con.cursor()
    curseur.execute('CREATE TABLE IF NOT EXISTS nombres_manquant (nombre INTEGER)')
    curseur.execute('INSERT INTO nombres_manquant VALUES (?)', (nmbr_manquant,))
    con.commit()
    con.close()
    return nmbr_manquant

tableau_test = [1, 2, 3, 4, 5, 6, 8]
print("Le nombre manquant est :", nombre_manquant(tableau_test))
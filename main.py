#### Imports et définition des variables globales
import csv
FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open (filename, "r", encoding = "utf-8") as fichier : # with permet de fermer le fichier, r pour read, encoding...pour les accents ou les caractères spéciaux
        lecteur = csv.reader(fichier,delimiter=';') # création d'un objet lecteur, ou avec ligne = fichier.readlines()
        for ligne in lecteur : # on parcourt les lignes du fichier
            l.append([int(i) for i in ligne]) # on ajoute la ligne à la liste
    return l

def get_list_k(data, k):
    if data == [] :
        return None
    L = data[k]
    return L

def get_first(L):
    if L == [] :
        return None
    first = L[0]
    return first

def get_last(L):
    if L == [] :
        return None
    last = L[-1]
    return last

def get_max(L):
    if L == [] :
        return None
    return max(map(float,L))

def get_min(L):
    if L == [] :
        return None
    return min(map(float,L))

def get_sum(L):
    if L == [] :
        return None
    return sum(map(float,L))

#### Fonction principale


def main():
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    l = get_list_k(data, 37)
    print(f'l {l}, first {get_first(l)}, last {get_last(l)}, max {get_max(l)}, min {get_min(l)}, sum {get_sum(l)}')
    


if __name__ == "__main__":
    main()

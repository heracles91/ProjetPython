# PROJET PYTHON
from time import sleep
style_lecture = \
    '''1. Science-fiction 
2. Biographie 
3. Horreur 
4. Romance 
5. Fable 
6. Histoire 
7. Comédie'''
genre={1:"Homme", 2:"Femme", 3:"Genre non renseigné"}
age={1:"Moins de 18ans", 2:"Entre 18 et 25ans", 3:"Plus de 25ans"}
style = {
    1: 'Science-Fiction',
    2: 'Biographie',
    3: 'Horreur',
    4: 'Romance',
    5: 'Fable',
    6: 'Histoire',
    7: 'Comedie',
    }

def verif_livre(livre:str)->bool:
    """Cette fonction vérifie la présence d'un livre
    Le nom du livre en parametre
    Renvoi True or False"""

    books = open('books.txt', 'r', encoding='utf-8')
    book = books.readlines()
    books.close()
    verif = False
    for ligne in book:
        if ligne[:len(ligne) - 1]  ==  livre:
            verif = True
    return verif

def verif_lecteur(lecteur:str)->bool:
    """Cette fonction vérifie la présence d'un lecteur
    Le pseudo du lecteur en paramètre
    Renvoi True or False"""

    readers = open('readers.txt', 'r')
    reader = readers.readlines()
    readers.close()
    verif = False
    for ligne in reader:
        test = ligne[:-1].split(',')
        if test[0]  ==  lecteur:
            verif = True
    return verif


def ajouter_lecteur():
    """Ajoute un lecteur à nos registre"""
    
    print("Ajout lecteur")
    pseudo = input("Entrer le pseudo: ")
    if verif_lecteur(pseudo)  ==  False:
        genre = int(input("1.HOMME | 2.FEMME | 3.PEU IMPORTE: "))
        #Saisie sécurisée
        while genre not in [1, 2, 3]:
            genre = int(input("1.HOMME | 2.FEMME | 3.PEU IMPORTE: "))

        #Saisie sécurisée
        age = int(input("1.MOINS 18ANS | 2.ENTRE 18-25 | 3.PLUS 25ANS: "))
        while age not in [1, 2, 3]:
            age = int(input("1.MOINS 18ANS | 2.ENTRE 18-25 | 3.PLUS 25ANS: "))

        #J'affiche les différents styles de lecture définis en haut
        print(style_lecture)
        style = int(input())
        #Partie livres lus
        booksread = []
        books = open('books.txt', 'r', encoding="utf-8").readlines()
        for i in range(len(books)):
            #J'affiche d'abord les livres lu ensuite je lui demande combien il en a lu et je crée une boucle pour qu'il les renseigne
            print("n°" + str(i + 1) + " " + books[i])
        test = int(input("Combien de livre avez-vous lu: "))
        for i in range(test):
            booksread.append(int(input("Veuillez les entrer un par un: ")) - 1)
        #J'ouvre le fichier readers.txt en a pour append
        fichier = open('readers.txt', 'a', encoding = "utf-8")
        fichier.write(str(pseudo)+","+str(genre)+","+str(age)+","+str(style)+'\n')
        fichier.close()

        fichier2 = open('booksread.txt', 'a', encoding="utf-8")
        fichier2.write(str(pseudo))
        for book in booksread:
            fichier2.write("," + str(book))
        fichier2.write('\n')
        fichier2.close()

        #j'ajoute un ligne à la matrice
        matrice.append(["" for x in books])

        if test>0: #Si test est supérieur à 0 ça veut dire qu'il a lu un livre
            veut_noter=int(input("Voulez-vous noter un livre que vous avez lu? Enter 1 pour OUI | 2 pour NON: "))
            while veut_noter not in [1, 2]:
                veut_noter=int(input("Veuillez entrer uniquement 1 ou 2: "))
            if veut_noter == 1:
                nombre_note=int(input("Combien de livre voulez-vous noter: "))
                while nombre_note<1 or nombre_note>test:
                    print("Veuillez entrer un chiffre entre 1 et", test, end=": ")
                    nombre_note=int(input())
                for i in range(nombre_note):
                    noter_livre(matrice, pseudo)
    else:
        print(pseudo, "est déjà présent dans nos registres.")
    sleep(2)
    menu()

def afficher_livres():
    """Affiche la liste des livres présents dans le dépôt"""

    print("Affichage livres")
    books = open('books.txt', 'r', encoding="utf-8")
    for ligne in books:
        print(ligne[:-1])
    books.close()
    sleep(2)
    menu()

def afficher_lecteur():
    """Affiche un lecteur donné s'il est présent dans nos registre"""

    print("Affichage lecteur")
    nom=input("Entrer le pseudo du lecteur: ")
    if verif_lecteur(nom):
        utilisateurs = open('readers.txt', 'r', encoding="utf-8")
        livres_lus = open('booksread.txt', 'r', encoding="utf-8")
        #Partie informations de l'utilisateur
        for ligne1 in utilisateurs:
            liste=ligne1.split(',')
            if liste[0] == nom:
                #J'ai défini des dico juste en haut, et le numéro trouvé dans le fichier
                #readers va afficher la valeur associée à cette clé
                print(nom, genre[int(liste[1])], age[int(liste[2])], style[int(liste[3][:-1])]) #[:-1] parce qu'à la fin il y avait \n qui me permettait de sauter une ligne
                #Partie livres lus par le lecteur
                for ligne2 in livres_lus:
                    liste2=ligne2[:-1].split(',')
                    if len(liste2)>1: #Si la taille est supérieure à 1 ça veut dire qu'il a lu 1 livre ou +
                        if liste2[0] == nom:
                            print("Livres lus: ")
                            for i in range(1, len(liste2)):#on part de 1 pour ne pas commencer au 0 qui est le pseudo
                                print(i)
                                with open('books.txt', 'r', encoding="utf-8") as livres:
                                    lignes2=livres.readlines()
                                print(lignes2[int(liste2[i])-1][:-1])
    else:
        print(nom, "n'est pas dans nos registres.")
    sleep(2)
    menu()

def modifier_lecteur():
    """Modifier un lecteur existant dans nos registres"""

    print("modification lecteur")
    nom=input("Entrer le pseudo du lecteur que vous voulez modifier: ")
    #Je vérifie d'abord si l'utilisateur existe dans readers.txt
    if verif_lecteur(nom):
        modifier=int(input("Que voulez vous modifier? \n1-> Ses informations personnelles \n2-> Ses livres lus \n3-> Les deux \nEntrer : "))
        
        if modifier == 1 or modifier == 3:
            #Je redemande toutes les informations
            pseudo=input("Entrer le pseudo: ")
            genre=int(input("1.HOMME | 2.FEMME | 3.PEU IMPORTE: "))
            age=int(input("1.MOINS 18ANS | 2.ENTRE 18-25 | 3.PLUS 25ANS: "))
            print(style_lecture)
            style=int(input())
            #la variable lecteurs va contenir le texte dans readers, ligne par ligne
            readers = open('readers.txt', 'r', encoding="utf-8")
            lecteurs = readers.readlines()
            readers.close()
            #Je split dans une variable temporaire et si le premier élément est le nom recherché
            for i in range(len(lecteurs)):
                test=lecteurs[i].split(',')
                if test[0] == nom:
                    del lecteurs[i] #je supprime la ligne qui contenait les anciennes info
                    lecteurs += str(pseudo)+','+str(genre)+','+str(age)+','+str(style)+'\n' #et écrit à la fin les nouvelles
            #je réécris le fichier avec la variable lecteurs qui contient les nouvelles infos
            readers = open('readers.txt', 'w+', encoding="utf-8")
            for lignes in lecteurs:
                readers.write(lignes)
            readers.close()
            
        if modifier == 2 or modifier == 3:
            #Je redemande quels livres ont été lus
            books = open('books.txt', 'r', encoding="utf-8")
            i=0
            for ligne in books:
                i += 1
                print("n°",i," ",ligne)
            books.close()
            
            nbr=int(input("Combien de livre avez-vous lu: "))
            booksread=[]
            for i in range(nbr):
                booksread.append(int(input("Veuillez les entrer un par un: ")))
            
            #La variable livres_lus va contenir le texte dans booksread
            livres_lus = open('booksread.txt', 'r', encoding="utf-8")
            livres=livres_lus.readlines()
            livres_lus.close()
            for i in range(len(livres)):
                test=livres[i].split(',')
                if len(test) == 1:
                    test[0]=test[0][:-1] #si la taille est égale à 1 ça veut dire que l'utilisateur n'a pas lu de livre donc il y aura '\n' à la fin de son pseudo alors je le remplace sans
                if test[0] == nom:
                    del livres[i]
                    if modifier == 2: #Si l'utilisateur n'a pas modifié le nom du lecteur
                        livres += nom #J'utilise la variable "nom"
                    else:
                        livres += pseudo #Sinon "pseudo"
                    for book in booksread:
                        livres += ','+str(book)
                    livres += '\n'
            livres_lus = open('booksread.txt', 'w+', encoding="utf-8")
            for lignes in livres:
                livres_lus.write(lignes)
            livres_lus.close()
    else:
        print(nom, "n'est pas dans nos registres.")
    sleep(2)
    menu()

def supprimer_lecteur():
    """Supprime un utilisateur de nos registres"""

    print("suppression lecteur")
    nom=input("Entrer le nom du lecteur à supprimer: ")
    users = open('readers.txt', 'r', encoding="utf-8")
    books = open('booksread.txt', 'r', encoding="utf-8")
    utilisateurs=users.readlines()
    livres_lus=books.readlines()
    users.close()
    books.close()

    trouvé = False

    for i in range(len(utilisateurs)):
        test=utilisateurs[i].split(',')
        if test[0] == nom:
            x=i #Je dois créer une variable temporaire et supprimer hors boucle car sinon cela crée une list index out of range
            trouvé = True
    if trouvé == False:
        print(nom, "n'est pas dans nos regisres.")
    else:
        del utilisateurs[x]

        #Je supprime la ligne de la matrice correspondant à son rang
        del matrice[x]
        
        users = open('readers.txt', 'w+', encoding="utf-8")
        for ligne in utilisateurs:
            users.write(ligne)
        users.close()
        
        for i in range(len(livres_lus)):
            test=livres_lus[i].split(',')
            if test[0] == nom:
                x=i
        del livres_lus[x]
        
        books = open('booksread.txt', 'w+', encoding="utf-8")
        for ligne in livres_lus:
            books.write(ligne)
        books.close()
    sleep(2)
    menu()

def ajouter_livre():
    """Ajouter un livre dans nos registres"""

    print("Ajout de livre")
    entree=input("Quelle livre souhaitez vous ajouter: ")
    books = open('books.txt', 'r', encoding="utf-8")
    book=books.readlines()
    books.close()
    if verif_livre(entree) == True:
        print("Ce livre est déjà dans nos registres")
    else:
        book += str(entree)+'\n'
        books = open('books.txt', 'w', encoding="utf-8")
        for ligne2 in book:
            books.write(ligne2)
        books.close()
        print("Livre ajouté")
        #J'ajoute une colonne à la matrice
        for i in range(len(matrice)):
            matrice[i].append('')
    sleep(2)
    menu()

def modifier_livre():
    """Modifie un livre s'il est présent dans nos registres"""

    print("Modifie un livre")
    entree=input("Quelle livre souhaitez vous modifier: ")
    books = open('books.txt', 'r', encoding="utf-8")
    book=books.readlines()
    books.close()
    if verif_livre(entree) == False:
        print("Ce livre n'rest pas dans nos registres")
    else:
        nvx_titre=input("Que voulez vous mettre comme titre: ")
        for i in range(len(book)):
            if entree == book[i][:len(book[i])-1]:
                x=i
        del book[x]
        book += nvx_titre+'\n'
        books = open('books.txt', 'w', encoding="utf-8")
        for ligne2 in book:
            books.write(ligne2)
        books.close()
        print("Livre modifié")
    sleep(2)
    menu()

def supprimer_livre():
    """Supprime un livre présent dans nos dépôts et des livres lus des lecteurs"""

    print("Supprime un livre")
    livre_nom=input("Entrer le nom du livre à supprimer: ")
    #J'ouvre tous les fichiers nécessaires
    books = open('books.txt', 'r', encoding="utf-8")
    book=books.readlines()
    books.close()
    booksread = open('booksread.txt', 'r', encoding="utf-8")
    bookread=booksread.readlines()
    booksread.close()
    if verif_livre(livre_nom):
        for i in range(len(book)):
            if book[i][:-1] == livre_nom: #[:-1] pour avoir la ligne sans le retour à la ligne '\n'
                x=i #Je stock la variable dans x car sinon j'aurais une erreur d'index out of range
        del book[x]
        for j in range(len(matrice)):
            del matrice[j][x]
        books = open('books.txt', 'w', encoding="utf-8")
        for line in book:
            books.write(line)
        books.close()

        lecteurs_modifiés=[] #Je crée une liste de tous les lecteurs auxquels on aura modifié leurs livres lus
        indice_a_suppr=[] #Je vais stocker les indices des lignes à supprimer
        for i in range(len(bookread)):
            test=bookread[i][:-1].split(',')
            if len(test)>1: #Si la taille est supérieur à 1 cela signifie que le lecteur a indiqué avoir lu des livres
                a_lu=False
                modifié=False
                for j in range(1, len(test)):
                    if test[j]  ==  str(x): #Si la position du livre "x" supprimé est dans les livres lus du lecteur
                        a_lu=True
                        modifié=True
                        y=j
                    if int(test[j])>x: #Si l'indice du livre est plus grand que celui supprimé
                        modifié=True
                        test[j]=int(test[j]) - 1
                if a_lu:
                    test.pop(y) #Je supprime alors la y-ième valeur de ma liste temporaire
                if modifié:
                    lecteurs_modifiés.append(test) #J'ajoute la liste avec les nouvelles valeurs
                    indice_a_suppr.append(i)
        for i in range(len(indice_a_suppr)):
            del bookread[indice_a_suppr[i] - i]
        for elt in lecteurs_modifiés:
            bookread += str(elt[0])
            for i in range(1, len(elt)):
                bookread += ","+str(elt[i])
            bookread += '\n'
        booksread = open('booksread.txt', 'w', encoding="utf-8")
        for line in bookread:
            booksread.write(line)
        booksread.close()
    else:
        print("Ce livre n'est pas présent dans nos registres")
    sleep(2)
    menu()

def creation_matrice()->list:
    """Cette fonction initialise une matrice de notation"""

    readers = open('readers.txt', 'r').readlines()
    books = open('books.txt', 'r').readlines()
    matrice=[["" for x in books] for y in readers] #Liste par comprehension
    return matrice

def noter_livre(matrice:list, pseudo=0)->list:
    """Permet à un utilisateur de noter un livre à condition qu'il l'ait déjà lu
    renvoi la liste mise à jour
    le pseudo, si non renseigné, est égal à 0"""

    print("Notation livre")
    if pseudo == 0:
        pseudo=input("Entrer le pseudo de l'utilisateur qui note: ")
    readers = open('readers.txt', 'r', encoding="utf-8")
    lecteurs=readers.readlines()
    books = open('books.txt', 'r', encoding="utf-8")
    livres=books.readlines()
    booksread = open('booksread.txt', 'r', encoding="utf-8")
    livres_lus=booksread.readlines()

    present=False
    for i in range(len(lecteurs)):
        test=lecteurs[i][:-1].split(',')
        if test[0] == pseudo:
            present=True
            numero_lecteur=i #Je stocke le n° du lecteur car j'en aurais besoin pour rentrer la note
    #Maintenant on sait si l'utilisateur est présent ou pas
    if present == False:
        print(pseudo, "n'est pas présent dans nos registres.")
    else:
        titre=input("Entrer le titre du livre que vous souhaitez noter: ")
        if verif_livre(titre) == False:
            print('"'+str(titre)+'"'+" n'est pas présent dans nos registres." )
        else:
            for i in range( len(livres) ):
                if livres[i][:-1] == titre:
                    numero_livre=i
            lu=False
            for line in livres_lus:
                test=line[:-1].split(',')
                if test[0] == pseudo:
                    if str(numero_livre) in test:
                        lu=True
            if lu == False:
                print("Vous n'avez pas lu "+'"'+titre+'".')
            else:
                print("Entre 1 (je n’ai pas aimé) à 5 (excellent),")
                note=int(input("veuillez entrer la note que vous souhaitez attribuer: "))
                matrice[numero_lecteur][numero_livre]=note
    return matrice
def menu():
    """Cette fonciton fait un menu qui sera démarré à chaque execution"""

    print("゜。+。゜゜。*。゜゜。＋。゜*゜。゜。+。゜゜。*。゜゜。＋。゜*゜。゜。+。゜")
    print("゜。+。Bienvenue dans notre système de recommandation de livres゜。+。゜")
    print("゜。+。゜゜。*。゜゜。＋。゜*゜。゜。+。゜゜。*。゜゜。＋。゜*゜。゜。+。゜")
    print("Que souhaitez vous effectuer?")
    action=int(input("1 pour des actions sur les LECTEURS | 2 pour les LIVRES | 3 pour FERMER le programme\nEntrer: "))
    while action not in [1, 2, 3]:
        action=int(input("Entrer soit 1 soit 2"))
    if action == 1:
        fonctions_noms={ajouter_lecteur:"Ajouter lecteur", afficher_lecteur:"Afficher lecteur", modifier_lecteur:"Modifier lecteur", supprimer_lecteur:"Supprimer lecteur"}
        fonctions={1:ajouter_lecteur, 2:afficher_lecteur, 3:modifier_lecteur, 4:supprimer_lecteur}
        for i in range(1, len(fonctions.values())+1):
            print("Entrer", i, "pour", fonctions_noms[fonctions[i]])
        fonctions[int(input(":"))]()
    elif action == 2:
        fonctions_noms={afficher_livres:"Afficher livre", ajouter_livre:"Ajouter livre", modifier_livre:"Modifier livre", supprimer_livre:"Supprimer livre"}
        fonctions={1:afficher_livres, 2:ajouter_livre, 3:modifier_livre, 4:supprimer_livre}
        for i in range(1, len(fonctions.values())+1):
            print("Entrer", i, "pour", fonctions_noms[fonctions[i]])
        fonctions[int(input(":"))]()
    else:
        print("Fermeture.")
matrice=creation_matrice()
menu()
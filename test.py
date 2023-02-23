from datetime import datetime 

# Function d'affichage du menu
def Affichermenu():
    print("#############################################\n"
          "###                                       ###\n"
          "###          PROGRAMME DE GESTION         ###\n"
          "###              DES PERSONNES            ###\n"
          "###                                       ###\n"
          "#############################################\n")

    print("1- Enregistrer une personne")
    print("2- Liste des personnes enregistrées")
    print("3- Rechercher un utilisateur par sa date d'enregistrement")
    print("4- Quitter \n")

# Function de demande 
def demanderMenu():
    menu = int(input("Faite votre choix :\n"))
    return menu

#fonction permettant d'enregistrer les informations entréés à l'inscription dans un fichier nommé liste.txt
def inscription():
    nom = input("Entrer votre nom: \n")
    prenom = input("Entrer votre prenom: \n")
    email = input("Entrer votre email: \n")
    contact = input("Entrer votre contact: \n")
    myDatetime = datetime.now()
    jour = myDatetime.strftime("%d/%m/%y")
    heure = myDatetime.strftime("%H:%M")
    info = f"{jour} {heure} {nom} {prenom} {email} {contact}\n"
    with open("liste.txt", "a+") as fichier:
        fichier.write(info)
        print("Enregistrement effectué ! \n")
    fichier.close() 


Affichermenu()
#menu = int(input("Taper:1 pour vous enregister,2 pour consulter la liste, 3 Rechercher un utilisateur ou 4 pour quitter\n"))
menu = demanderMenu()

match menu:
    case(1):
        inscription()
        print("Voulez vous continuer? \n")
        tryagain = int(input("1 pour oui et 2 pour non \n"))
        while tryagain == 1:
            Affichermenu()
            menu = int(input("Taper:1 pour vous enregister,2 pour consulter la liste, 3 Rechercher un utilisateur ou 4 pour quitter\n"))
            inscription()

        if tryagain == 2:
            print("Aurevoir")

        if tryagain != 1 & tryagain != 2:
            print("Vous avez entré le mauvais chiffre")
            Affichermenu()
            inscription()
        
        
    case(2):
        with open("liste.txt", "r") as fichier:
            print("liste du fichier:")
            for x in fichier:
                print(x)
            fichier.close()


    case(3):
       chaine = input("Entrer la date exemple: 01/01/2023 \n") 
       fichier = open("liste.txt","r")
       for ligne in fichier:
         if chaine in ligne:
           print (ligne)
       fichier.close()

    case(4):
      print("Au revoir")
    





            
        

        

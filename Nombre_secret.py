from random import *


print("Bienvenue dans le jeu du nombre secret")
rules=(str(input("Voulez-vous qu'on vous rappelle les règles?")))
      
if rules in ['oui', 'o', 'y', 'yes', 'ouais', 'ok']:
    print("Le but du jeu est de trouver un nombre comprit entre une intervalle, selon le mode choisit")
   
   
    
mode = (int(input("Quel mode de jeu voulez vous ? \n 1 : Facile \n 2: Intermédiaire \n 3: Difficile \n")))
        
if mode == 1 :
    number = int(input("Entrez un nombre :"))
    secret_number = randint(0, 100)
    c = 0
    while number != secret_number :              
        c = c + 1
        if number > secret_number :
            print("Le nombre est trop grand, vous êtes à", c, "coup(s) ! \n")
                                 
        else :
            print("Le nombre est trop petit, vous êtes à", c, "coup(s) ! \n")
        number = int(input("Entrez un nombre :"))
                    
    print("Bien joué!")
            
if mode == 2 :
    number = int(input("Entrez un nombre :"))
    secret_number = randint(0, 1000)
    c = 0
    while number != secret_number :              
        c = c + 1
        if number > secret_number :
            print("Le nombre est trop grand, vous êtes à", c, "coup(s) ! \n")
                                 
        else :
            print("Le nombre est trop petit, vous êtes à", c, "coup(s) ! \n")
        number = int(input("Entrez un nombre :"))
                    
    print("Bien joué!")
            
if mode == 3 :
    number = int(input("Entrez un nombre :"))
    secret_number = randint(0, 10000)
    c = 0
    while number != secret_number :              
        c = c + 1
        if number > secret_number :
            print("Le nombre est trop grand, vous êtes à", c, "coup(s) ! \n")
                                 
        else :
            print("Le nombre est trop petit, vous êtes à", c, "coup(s) ! \n")
        number = int(input("Entrez un nombre :"))
                    
    print("Bien joué!")
            
    
            
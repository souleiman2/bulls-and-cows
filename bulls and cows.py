import math#module que j'ai besoin pour la fonction floor
import random#module que j'ai besoin pour la fonction random

#remplie dans la liste combinaison (toutes les possibilités de choix à prendre)
combinaison=[]
for i in range(10):
        for j in range(10):
                for k in range(10):
                        for l in range(10):
                            if i!=j and i!=k and i!=l and j!=k and j!=l and k!=l:
                                temp=str(i)+str(j)+str(k)+str(l)
                                combinaison.append(temp)
                                

#répète le jeux pour pouvoir y jouer de nombreuses fois
while True:
        possibilité_ordi=combinaison[:] #faire une copie de la liste pour pouvoir éléminer des choix
        nombre_ordi=combinaison[(math.floor(random.random()*len(combinaison)))]#choisit dans les différentes combinaisons un nombre qui sera celui de l'ordinateur
        fini=False#pour répéter le fait que l'utilisateur donne un nombre et fait des actions
        tour=True#pour que l'utilisateur commence avec le tour
        while not fini:
                if tour:
                    bon=False
                    #répéter le fait que l'utilisateur donne un nombre jusqu'à ce que ce nombre soit adéquat
                    while not bon:
                        reponse=str(input("Quel est le nombre que vous devinez: "))
                        if reponse in combinaison:
                            bon=True
                        else:
                                print("Veuillez sélectionner un bon nombre")
                #reinitialise les bulls et les cows pour savoir ceux individuellement
                    bulls=0
                    cows=0
                    #compter les bulls et les cows
                    i=0
                    for i in range(4):
                        if reponse[i] in nombre_ordi:
                            if reponse[i]==nombre_ordi[i]:
                                bulls+=1
                            else:
                                cows+=1
                    #indique à l'utilisateur combien de bulls et de cows il y a eut pour le nombre
                    print("Voici le nombre de bulls: "+ str(bulls))
                    print("Voici le nombre de cows: "+ str(cows))
                    #condition d'arrêt si l'utilisateur a gagné
                    if bulls==4:
                        print("Bravo vous avez gagné")
                        print("Rematch!")
                        fini=True
                else:
                     choix_ordi=possibilité_ordi[(math.floor(random.random()*len(possibilité_ordi)))]#l'ordinateur choisit un nombre qui se trouve dans la liste possibilité_ordi
                     print("Moi je choisit le nombre :" + choix_ordi)#indique à l'utilisateur quel numéro l'ordi a fait
                     bon=False
                     while not bon:
                        #l'utilisateur doit donner de bon nombre de bulls et de cows
                        choix_bulls=input("Le nombre de bulls :")
                        choix_cows=input("Le nombre de cows :")
                        #regarde si le nombre de bulls et de cows est possible
                        if int(choix_bulls)+int(choix_cows)>4:
                                print("Hum cela n'est pas possible, réessayer")
                        elif int(choix_bulls)==4:
                                bon=True
                                fini=True
                                print("Ah j'tait niquer connard!!")
                        else:
                                bon=True
                                i=0
                                possibilité_ordi_oui=[]
                                #print(str(choix_bulls)+str(choix_cows))
                                while i!=len(possibilité_ordi)-1:
                                        nbre_bulls=0
                                        nbre_cows=0
                                        j=0
                                        je_sais_pas=""
                                        je_sais_pas=possibilité_ordi[i]
                                        for j in range(4):
                                                if je_sais_pas[j] in choix_ordi:
                                                      if je_sais_pas[j] in choix_ordi[j]:
                                                         nbre_bulls+=1
                                                      else:
                                                         nbre_cows+=1
                                        if nbre_bulls==int(choix_bulls) and nbre_cows==int(choix_cows):
                                                possibilité_ordi_oui.append(possibilité_ordi[i])
                                        i+=1
                                possibilité_ordi=possibilité_ordi_oui[:]
                                #print(possibilité_ordi
                                if len(possibilité_ordi)==0:
                                        print("Cela est impossible tu as mentit quelque part")
                                        bon=True
                                        fini=True
                tour=not tour
        print("Rematch!")
    
    

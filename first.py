# fichier=open("test1.py")  #Premiere maniere d'ouvrir le fichier
# for ligne in fichier:     #parcourir tous les infos du fichiers
#     print(ligne.strip())  #Afficher tous les lignes de notre fichier
# fichier.close()           #Fermer le fichier le fichier apres lecture
# ###############################
# with open("test1.py","r") as fichier:# Une autre maniere de lire le fichier
#     for ligne in fichier: # Parcourir les infos de notre fichier 
#         print(ligne.strip()) # Afficher les differentes infos de notre fichier
#                          #on a pas besoin de close apres la fonction with.
# ##########################################

fichier=open("test1.py","w")# On ouvre le fichier avec  l'ecriture w=writte
fichier.write("Bonjour tous P3 Simplon") #On ecrit dans le fichier 
fichier.close()#On ferme le fichier apres usage
###########################
fichier=open("test1.py","r") #On ouvre le fichier avec r=read
for ligne in fichier:    # On parcour les infos du fichier pour les utilise
    print(ligne.strip()) # On affiche les informations contenuent dans notre fichier
fichier.close()  # On ferme le fichier apres usage

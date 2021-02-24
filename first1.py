fichier=open("test1.py","a") #On ouvre le fichier avec a=append
fichier.write("\n")          #"/n" sa signifie aller a la ligne pour ouverture avec append
fichier.write("Nous sommes de la P3") #On ajoute le message au fichier test1
fichier.write("\n")
fichier.write("On va terminer bientot")
fichier.close()

fichier=open("test1.py","r")
for ligne in fichier:
    print(ligne.strip())
fichier.close()
####__ Comment lire un fichier zipper dans le repertoir courant __####
from zipfile import ZipFile 
  
# spécifiant le nom du fichier zip
file = "archive.zip"
  
# ouvrir le fichier zip en mode lecture
with ZipFile(file, 'r') as zip: 
    # afficher tout le contenu du fichier zip
    zip.printdir() 
  
    # extraire tous les fichiers
    print('extraction...') 
    zip.extractall() 
    print('Terminé!')

########___Autre methode pour lire un fichier zipper dans un repertoir specifique __##########
from zipfile import ZipFile 
  
# spécifiant le nom du fichier zip

file = "archive.zip"
####__ouvrir le fichier zip en mode lecture___####
with ZipFile(file, 'r') as zip: 
    # extraire tous les fichiers vers un autre répertoire
    zip.extractall('zip_destination')
#######__Extraire un seul fichier zip__###
import zipfile
         
zip = zipfile.ZipFile('C:\\User\\wtlx\\archive.zip')
zip.extract('logo.jpg', 'C:\\User\\wtlx')
 
zip.close()
#####____fin du processus_______##########
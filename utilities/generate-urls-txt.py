#This program automatically generates the list with URLs
#We assume image files follow the standard pattern of uploads in Wordpress
#Limitations: This will list all files in the folder, regardless if t
#Author: orlando.academy

#Paso 1: Lista de los archivos del directorio
from os import listdir
from os.path import isfile, join
from os import walk

#Path of the main folder with the products subfolder
path_main = "G:\My Drive\Electronica Club\Productos - Fase 3"

#Prefix of the image URLs, or URL pattern
url_pattern = "https://electronica.club/wp-content/uploads/2021/07/"

f = []
for (dirpath, dirnames, filenames) in walk(path_main):
    f.extend(filenames)
    break

for d in dirnames:
    direc_actual = str(path_main + "\\" + d)
    onlyfiles2 = [f for f in listdir(direc_actual) if isfile(join(direc_actual, f))]
    onlyfiles2.pop()
    fop = open(path_main + "\\" + d + "\\" + d + ".txt", 'w')
    for file_single in onlyfiles2:
        fop.write( url_pattern + file_single + ", ")
    fop.close()

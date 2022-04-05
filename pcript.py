# mon_text = open("dossier_text/Mon_text_lorem.txt")
# content = mon_text.read()
# print(content)

# mon_text.close()

########################################################################

# mon_text = open("dossier_text/Mon_text_lorem.txt")

# ligne = mon_text.readline()
# for line in mon_text :
#     print(ligne)

# mon_text.close()
#######################################################################
#
# Lecteur de Texx ####################################
# /#
# créer une function 
def lecteur_text (nmb_ligne):
    #ouvrir le dossier à lire
    dossier_a_lire = open("./dossier_text/Mon_text_lorem.txt")
    # mettre le conteur à 0
    count = 1
    # la ligne à trouvée / False départ
    ligne_choisi = False
    # loop for pour définir quelle ligne l'utilisateur demande loop variable dans le text à lire 
    for lignes_dans_text in dossier_a_lire :
        #condition comparer numéro de et conteur
        if count == nmb_ligne:
             # ligne trouvé est vrais
            ligne_choisi = True
            print(lignes_dans_text)
        #quitte le loop
            break
        count +=1
    # si la ligne demandée n'ai pas trouvé
    if not ligne_choisi:
        print("Cette ligne n'existe pas")
    dossier_a_lire.close()
# lire d'autre ligne
def continue_a_lire ():
    answer = input("Veut-tu continuer à lire (yes ou oui) ? ")
    return (answer == "yes" or answer == "oui")
#Répéter autant qu'on veut que l'utilisateur puisse jouer.. looping while
continue_loop = True
while continue_loop :
    user_ligne = int(input("Quelle ligne souhaites-tu afficher ? "))
    lecteur_text(user_ligne)
    continue_loop = continue_a_lire()
######################################################################################


















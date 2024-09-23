import os
import json
is_on = True
liste_de_course = []
dossier_courant = os.path.dirname(__file__)


while is_on:
    while True:
        try:
            menu = int(input("1️⃣: ajouter un élément à la liste.\n"
                             "2️⃣: retirer un élément de la liste.\n"
                             "3️⃣: afficher la liste.\n"
                             "4️⃣: vider la liste.\n"
                             "5️⃣: quitter.\n"
                             "👉: votre choix: "))

            if menu == 1:
                ajout = input("Veuillez saisir un élément a ajouter: ")
                liste_de_course.append(ajout)
                with open(dossier_courant + "/liste_de_course.json", "w", encoding="utf-8") as file:
                    json.dump(liste_de_course, file, indent=4, ensure_ascii=False)
                print(f"'{ajout}' a été ajouté à la liste de course 🛒\n"
                      f"Voici la nouvelle liste {liste_de_course}🛍️. ")
                continue

            elif menu == 2:
                element_retire = input("Veuillez saisir l'élément a retirer: ")
                if element_retire in liste_de_course:
                    liste_de_course.remove(element_retire)
                    with open(dossier_courant + "/liste_de_course.json", "w", encoding="utf-8") as file:
                        json.dump(liste_de_course, file, indent=4, ensure_ascii=False)
                    print(f"'{element_retire}' a été retiré de la liste de course 🛒\n"
                          f"Voici la nouvelle liste {liste_de_course}🛍️. ")
                    continue
                else:
                    print("‼️ L'élément saisie n'est pas dans la liste de course. ")
                    continue

            elif menu == 3:
                with open(dossier_courant + "/liste_de_course.json", "r") as file:
                    liste_de_course = json.load(file)
                print(liste_de_course)
                continue

            elif menu == 4:
                liste_de_course.clear()
                with open(dossier_courant + "/liste_de_course.json", "w") as file:
                    json.dump(liste_de_course, file, indent=4)
                print("La liste de course a été vidé. ")

            elif menu == 5:
                is_on = False
                break

            elif menu not in [1, 2, 3, 4, 5]:
                raise ValueError

        except ValueError:
            print("⚠️ Veuillez choisir entre l'option 1 et 5.")

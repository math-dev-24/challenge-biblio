LIST_COMMANDS: (str, ...) = (
    "Ajouter un livre", "Supprimer un livre", "Modifier un livre", "Emprunter un livre", "Retourner un livre",
    "Lister les livres", "Statistiques", "Quitter"
)

if __name__ == "__main__":

    print("Bienvenue dans la bibliothèque")

    while True:
        for i, command in enumerate(LIST_COMMANDS):
            print(f"{i + 1}. {command}")

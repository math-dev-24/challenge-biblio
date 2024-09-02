from Core.printer import Message
from Core.book import create_book

LIST_COMMANDS: (str, ...) = (
    "Ajouter un livre", "Supprimer un livre", "Modifier un livre", "Emprunter un livre", "Retourner un livre",
    "Lister les livres", "Statistiques", "Quitter"
)

if __name__ == "__main__":

    Message.title("Ma bibliothèque")

    while True:
        for i, command in enumerate(LIST_COMMANDS):
            print(f"{i + 1}. {command}")

        Message.question("Que voulez-vous faire ?")
        action: str = Message.input()

        if action == "1":
            create_book()
        elif action == "2":
            print("Supprimer un livre")
        elif action == "3":
            print("Modifier un livre")
        elif action == "4":
            print("Emprunter un livre")
        elif action == "5":
            print("Retourner un livre")
        elif action == "6":
            print("Lister les livres")
        elif action == "7":
            print("Statistiques")
        elif action == "8":
            Message.info("Au revoir")
            break
        else:
            Message.warning("Commande non reconnue")
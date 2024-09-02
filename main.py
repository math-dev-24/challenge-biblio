from Core.printer import Message
from Controller.BookController import BookController
LIST_COMMANDS: (str, ...) = (
    "Ajouter un livre", "Supprimer un livre", "Modifier un livre", "Emprunter un livre", "Retourner un livre",
    "Lister les livres", "Statistiques", "Quitter"
)

if __name__ == "__main__":
    bookController = BookController()

    Message.title("Ma bibliothèque")

    while True:
        for i, command in enumerate(LIST_COMMANDS):
            print(f"{i + 1}. {command}")

        Message.question("Que voulez-vous faire ?")
        action: str = Message.input()

        if action == "1":
            bookController.create_book()
        elif action == "2":
            print("Supprimer un livre")
        elif action == "3":
            print("Modifier un livre")
        elif action == "4":
            print("Emprunter un livre")
        elif action == "5":
            print("Retourner un livre")
        elif action == "6":
            bookController.get_all_books()
        elif action == "7":
            print("Statistiques")
        elif action == "8":
            Message.info("Au revoir")
            break
        else:
            Message.warning("Commande non reconnue")
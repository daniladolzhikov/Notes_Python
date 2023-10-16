from loggers import add_note, list_notes, edit_note, delete_note

def main():
    while True:
        print("\nМеню:")
        print("1. Список заметок")
        print("2. Добавить заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")
        print()
        choice = input("Выберите действие: ")

        if choice == '1':
            list_notes()
        elif choice == '2':
            add_note()
        elif choice == '3':
            edit_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
    